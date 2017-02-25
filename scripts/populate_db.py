# -*- coding: utf-8 -*-

from workload.database import db_session, init_db
from workload.models import Job

def populate():
    """ Populates the database with some examples."""

    jobs = [Job(id=1, status='queued', function='lambda x, y: x + y', function_args='[1, 2]'),
            Job(id=2, status='queued', function='lambda x, y: pow(x, y)', function_args='[3, 5]'),
            Job(id=3, status='queued', function='lambda x: "init_" + x + "_end"', function_args='"[middle,]"'),
            Job(id=4, status='queued', function='lambda x, y: x * y', function_args='[5, 9]')]
    session = db_session()

    for j in jobs:
        session.add(j)
    session.commit()
    session.close()

if __name__ == "__main__":
    init_db()
    populate()
