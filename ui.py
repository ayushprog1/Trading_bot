import tkinter as tk
from tkinter import ttk, messagebox
from bot.orders import place_order

class TradingBotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Primetrade.ai - Trading UI")
        self.root.geometry("400x450")
        self.root.configure(padx=20, pady=20)

        self.symbol = tk.StringVar(value="BTCUSDT")
        self.side = tk.StringVar(value="BUY")
        self.type = tk.StringVar(value="MARKET")
        self.qty = tk.StringVar(value="0.01")
        self.price = tk.StringVar()
        self.stop_price = tk.StringVar()

        self.build_ui()

    def build_ui(self):
        ttk.Label(self.root, text="Binance Futures Bot", font=("Arial", 14, "bold")).pack(pady=10)
        
        form = ttk.Frame(self.root)
        form.pack(fill=tk.X)

        fields = [
            ("Symbol:", self.symbol, ttk.Entry),
            ("Side:", self.side, ttk.Combobox, ["BUY", "SELL"]),
            ("Type:", self.type, ttk.Combobox, ["MARKET", "LIMIT", "STOP"]),
            ("Quantity:", self.qty, ttk.Entry),
            ("Price:", self.price, ttk.Entry),
            ("Stop Price:", self.stop_price, ttk.Entry),
        ]

        for i, field in enumerate(fields):
            ttk.Label(form, text=field[0]).grid(row=i, column=0, sticky=tk.W, pady=5)
            if len(field) == 4:
                widget = field[2](form, textvariable=field[1], values=field[3], state="readonly")
            else:
                widget = field[2](form, textvariable=field[1])
            widget.grid(row=i, column=1, sticky=tk.EW, pady=5)

        ttk.Button(self.root, text="Execute Order", command=self.execute).pack(fill=tk.X, pady=20)

    def execute(self):
        try:
            qty = float(self.qty.get())
            prc = float(self.price.get()) if self.price.get() else None
            stp = float(self.stop_price.get()) if self.stop_price.get() else None
            
            res = place_order(self.symbol.get(), self.side.get(), self.type.get(), qty, prc, stp)
            
            # THE FIX: Check for standard orderId OR the new algoId
            if "orderId" in res or "algoId" in res:
                order_id = res.get('orderId', res.get('algoId'))
                status = res.get('status', res.get('algoStatus'))
                messagebox.showinfo("Success", f"Order Placed!\nID: {order_id}\nStatus: {status}")
            else:
                messagebox.showerror("Error", res.get('msg', res.get('error', 'Unknown Error')))
        except ValueError:
            messagebox.showerror("Input Error", "Please check your number inputs.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TradingBotUI(root)
    root.mainloop()