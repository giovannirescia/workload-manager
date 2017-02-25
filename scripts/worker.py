# -*- coding: utf-8 -*-
""" This script looks for queued tasks and executed, one at the time."""

import argparse

from sqlalchemy.orm import scoped_session, sessionmaker

from workload.models import Job
from workload.database import db_session, db_connect


def execute_task(node_address='0.0.0.0'):

    session = db_session()
    job = session.query(Job).filter_by(status='queued').first()
    if job is not None:
        job.status = "running"
        session.commit()
        try:
            function = eval(job.function)
            args = eval(job.function_args)
            res = function(*args)
            job.result = res
            job.status = "completed"
            job.node = node_address
        except:
            job.status = "failed"
            session.commit()
        session.commit()

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Runs this script for executing tasks",
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    arg_parser.add_argument("-N", "--node", type=str,
                            default="0.0.0.0", help="From which node a task is being executed")

    args = vars(arg_parser.parse_args())
    node_address = args["node"]
    execute_task(node_address=node_address)
