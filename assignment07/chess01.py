import asyncio
import time

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 3
move_pairs = 30

async def game(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        # Simulate thinking time for Judit
        await asyncio.sleep(my_compute_time)
        print(f"BOARD-{x+1} {i+1} Judit made a move.")
        
        # Simulate thinking time for the opponent
        await asyncio.sleep(opponent_compute_time)
        print(f"BOARD-{x+1} {i+1} Opponent made a move.")
    
    elapsed_time = time.perf_counter() - board_start_time
    print(f"BOARD-{x+1} - >>>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter())} ")
    return round(elapsed_time)

async def main():
    start_time = time.perf_counter()
    
    # Run the games asynchronously
    board_tasks = [game(board) for board in range(opponents)]
    board_times = await asyncio.gather(*board_tasks)
    
    board_time = sum(board_times)
    print(f"Board exhibition finished in {board_time} secs.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")

# Run the asynchronous main function
asyncio.run(main())
