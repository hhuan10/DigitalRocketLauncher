'''
   Author:  YiHang Huang
   Purpose: Main entry point for the Digital Rocket Launcher
   Digital Rocket Launcher is a simple math game that generates random math problems for the user to solve.
   Created: 2024.4.5
'''
import asyncio
from src.rocket import DigitalRocketLauncher

if __name__ == "__main__":
    asyncio.run(DigitalRocketLauncher().start())