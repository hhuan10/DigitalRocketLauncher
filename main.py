'''
   Author:  YiHang Huang
   Purpose: Main entry point for the MathGame
   MathGame is a simple math game that generates random math problems for the user to solve.
   Created: 2024.4.5
'''
import asyncio
from src.math import MathGame

if __name__ == "__main__":
    asyncio.run(MathGame().start())