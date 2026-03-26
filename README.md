# Primetrade.ai - Python Developer Intern Assignment

A robust, structured CLI and UI trading bot that interacts with the Binance Futures Testnet (USDT-M). This application places MARKET, LIMIT, and STOP (Stop-Limit) orders using direct REST API calls secured by HMAC SHA256 signatures.

## Project Structure
- `cli.py`: The main command-line interface entry point using Typer.
- `ui.py`: A lightweight graphical interface built with Tkinter.
- `bot/client.py`: Handles the core Binance API connection, server-time synchronization, and request signing.
- `bot/orders.py`: Core logic for constructing the order payloads.
- `bot/validators.py`: Strict input validation before API execution.
- `bot/logging_config.py`: Structured logging to a local file.

## Setup Steps
1. **Clone or Extract the Repository:**
   Navigate into the project directory:
   
       cd prime_trading_bot

2. **Create a Virtual Environment:**
   
       python -m venv venv
       # On Windows:
       .\venv\Scripts\activate
       # On Mac/Linux:
       source venv/bin/activate

3. **Install Dependencies:**
   
       pip install -r requirements.txt

4. **Environment Variables:**
   Create a `.env` file in the root directory and add your Binance Testnet credentials:
   
       BINANCE_TESTNET_API_KEY=your_api_key_here
       BINANCE_TESTNET_SECRET_KEY=your_secret_key_here

## How to Run Examples
Ensure your virtual environment is active. You can use the CLI or the UI.

**Method 1: Lightweight UI (Bonus)**
Launch the desktop application:
    
    python ui.py

**Method 2: Enhanced CLI (Bonus)**
The CLI accepts the following format:
`python cli.py [SYMBOL] [SIDE] [ORDER_TYPE] [QUANTITY] --price [PRICE] --stop-price [STOP_PRICE]`

*Example A: Execute a MARKET Buy Order*
    
    python cli.py BTCUSDT BUY MARKET 0.01

*Example B: Execute a LIMIT Sell Order*
    
    python cli.py BTCUSDT SELL LIMIT 0.01 --price 95000

*Example C: Execute a STOP (Stop-Limit) Sell Order (Bonus)*
    
    python cli.py BTCUSDT SELL STOP 0.01 --price 89500 --stop-price 90000

*Note: All API interactions are recorded locally in `bot_activity.log`.*

## Bonuses Completed
1. **Third Order Type:** Implemented `STOP` (Stop-Limit) logic securely alongside MARKET and LIMIT.
2. **Enhanced CLI:** Added secondary optional parameters (`--stop-price`) and robust terminal validation using Typer.
3. **Lightweight UI:** Included `ui.py` using Tkinter to provide a graphical interface option for rapid testing.

## Assumptions & Design Choices
1. **Direct REST Implementation:** Instead of relying on the `python-binance` wrapper, I chose to implement direct REST calls (`requests`) to demonstrate a deep, low-level understanding of API authentication, HMAC signatures, and payload construction.
2. **Server Time Synchronization:** To prevent standard "timestamp ahead of server" errors caused by local machine desync, `client.py` dynamically fetches the exact Binance server time before signing the request.