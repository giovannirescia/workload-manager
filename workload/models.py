# -*- coding: utf-8 -*-

"""The Models -Tables- for this database model."""
from sqlalchemy import (Column, Integer, String, DateTime, ForeignKey)
from sqlalchemy.orm import relationship, backref

from workload.database import Base


class Job(Base):
    """ Jobs table."""
    __tablename__ = "job"
    id = Column(u'id', Integer, primary_key=True)

    status = Column(u'status', String)
    node = Column(u'node', String)
    result = Column(u'result', String)
    function = Column(u'function', String)
    function_args = Column(u'function_args', String)

    def __repr__(self):
        return "<Job(id={}, status={}, node={}, result={}, function={}, function_args={})>".format(self.id,
                                                                                                   self.status,
                                                                                                   self.node,
                                                                                                   self.result,
                                                                                                   self.function,
                                                                                                   self.function_args)
