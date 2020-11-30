import os
import sys

src_abs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), r"..\src")
sys.path.append(src_abs_path)
import sakado



def before_all(context):
    context.application = sakado.Sakado("database.db", database_path=src_abs_path)