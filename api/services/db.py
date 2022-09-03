"""PRISMA"""
from prisma import Prisma

db = Prisma(use_dotenv=True,auto_register=True)
