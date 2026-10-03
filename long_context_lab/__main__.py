from argparse import ArgumentParser
from pathlib import Path
import json

from .io import read_jobs,read_rows,write_rows
from .ollama import OllamaRunner
from .planner import expand
from .report import summarize
from .runner import execute


def main():
    parser=ArgumentParser()
    sub=parser.add_subparsers(dest="cmd",required=True)

    plan=sub.add_parser("plan")
    plan.add_argument("config")

    run=sub.add_parser("run")
    run.add_argument("plan")
    run.add_argument("--model",required=True)
    run.add_argument("--out",required=True)
    run.add_argument("--endpoint",default="http://127.0.0.1:11434")

    report=sub.add_parser("report")
    report.add_argument("path")

    args=parser.parse_args()
    if args.cmd=="plan":
        config=json.loads(Path(args.config).read_text())
        for job in expand(config):
            print(json.dumps(job.to_dict(),sort_keys=True))
    elif args.cmd=="run":
        backend=OllamaRunner(args.model,args.endpoint)
        rows=[execute(job,backend) for job in read_jobs(args.plan)]
        write_rows(args.out,rows)
        print(json.dumps({"completed":len(rows)}))
    else:
        print(json.dumps(summarize(read_rows(args.path)),indent=2))


if __name__=="__main__":
    main()
