import asyncio
import random


# code explanation
# In this example, we define two asynchronous functions: fetch_data_from_api and process_data. 
# The fetch_data_from_api function simulates fetching data from an API by sleeping for a random duration between 0.5 and 2.0 seconds. 
# The process_data function simulates processing the data by sleeping for a random duration between 1.0 and 3.0 seconds. 
# The main async function first fetches data from the API asynchronously and then processes the data asynchronously.
# The asyncio.run function is used to run the main async function.


# Asynchronous function to fetch data from an API (simulated)
async def fetch_data_from_api():
    # Simulate fetching data (e.g., from a database or external API)
    # Simulate varying response times
    await asyncio.sleep(random.uniform(0.5, 2.0))
    return {"message": "Data fetched successfully"}

# Asynchronous function to process data


async def process_data(data):
    # Simulate data processing
    await asyncio.sleep(random.uniform(1.0, 3.0))  # Simulate processing time
    processed_data = {"processed_message": data["message"] + " and processed"}
    return processed_data

# Asynchronous main function


async def main():
    # Fetch data from the API asynchronously
    data = await fetch_data_from_api()
    print("Data fetched:", data)

    # Process the data asynchronously
    processed_data = await process_data(data)
    print("Processed data:", processed_data)

# Run the main async function
asyncio.run(main())
