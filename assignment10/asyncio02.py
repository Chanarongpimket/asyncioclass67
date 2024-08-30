from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    start_times = time.time()

    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all-done signal
    await queue.put(None)
    print('Producer: Done')

    end_times = time.time()
    total_time = end_times - start_times
    return total_time

# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    print('Consumer: Done')

# entry point coroutine
async def main():
    # start time for the entire program
    program_start_time = time.time()
    # create the shared queue
    queue = asyncio.Queue(maxsize=0)
    # run the producer and consumers
    producer_time = await asyncio.gather(producer(queue), consumer(queue))
    # end time for the entire program
    program_end_time = time.time()

    print(f'Total time taken by producer: {producer_time[0]:.4f} seconds')
    print(f'Total time of the entire program: {program_end_time - program_start_time:.4f} seconds')

# start the asyncio program
asyncio.run(main())
