import typer
from bot.orders import place_order

app = typer.Typer(help="Primetrade.ai - Binance Futures Trading Bot")

@app.command()
def trade(
    symbol: str = typer.Argument(..., help="Trading pair, e.g., BTCUSDT"),
    side: str = typer.Argument(..., help="BUY or SELL"),
    order_type: str = typer.Argument(..., help="MARKET, LIMIT, or STOP"),
    quantity: float = typer.Argument(..., help="Amount to trade"),
    price: float = typer.Option(None, "--price", "-p", help="Price required for LIMIT/STOP orders"),
    stop_price: float = typer.Option(None, "--stop-price", "-sp", help="Stop price required for STOP orders")
):
    typer.secho("\n--- Order Request Summary ---", fg=typer.colors.CYAN)
    typer.echo(f"Symbol: {symbol.upper()} | Side: {side.upper()} | Type: {order_type.upper()} | Qty: {quantity}")
    if price: typer.echo(f"Price: {price}")
    if stop_price: typer.echo(f"Stop Price: {stop_price}")
        
    typer.echo("\nExecuting order on Binance Testnet...")
    response = place_order(symbol, side, order_type, quantity, price, stop_price)
    
    typer.secho("\n--- Order Response Details ---", fg=typer.colors.CYAN)
    
    # Handle both standard Orders and Algo Orders
    if "orderId" in response or "algoId" in response:
        typer.secho("✅ SUCCESS: Order placed successfully!", fg=typer.colors.GREEN)
        
        # Print whichever ID and Status the exchange returned
        order_id = response.get('orderId', response.get('algoId'))
        status = response.get('status', response.get('algoStatus'))
        
        typer.echo(f"Order ID: {order_id}")
        typer.echo(f"Status: {status}")
        
        if 'executedQty' in response:
            typer.echo(f"Executed Qty: {response.get('executedQty')}")
    else:
        typer.secho("❌ FAILURE: Order could not be placed.", fg=typer.colors.RED)
        typer.echo(f"Error Message: {response.get('msg', response.get('error', 'Unknown Error'))}")

if __name__ == "__main__":
    app()