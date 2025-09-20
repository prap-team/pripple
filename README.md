# pripple, Ripple Wrapper for RWA and Payments

A Ripple-based STO (RWA) exchange wrapper.  
This project uses **RLUSD** as the main settlement currency.  

---

## 🧪 Sample

![Screenshot](https://drive.google.com/uc?id=1uWDGS8EQHO1kCrrBxwQ1WVCBWgOZBIAU)
[![Demo](https://drive.google.com/uc?id=1uWDGS8EQHO1kCrrBxwQ1WVCBWgOZBIAU)](https://drive.google.com/uc?id=1uWDGS8EQHO1kCrrBxwQ1WVCBWgOZBIAU)


## 🚀 Example

```python
from pripple import XRPLClass

# Use Testnet
client = XRPLClass()

# Get Wallet, if blank get a new wallet
wallet = client.get_account("seed")

# Get info
account_info = client.get_account_info(wallet.address)

# Send 1 xrp
result = client.send_xrp("from seed", 1, "destination seed")

```

## ⚙️ Setup
```bash
pip install git+https://github.com/prap-team/pripple.git
```

## 🙏 Credits
  
- [@seuljaa](https://github.com/seuljaa)  
- [@Parkayun](https://github.com/Parkayun)
- 
