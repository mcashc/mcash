all: wallet
	@echo "============="

wallet: ./src/wallet.py
	python3 ./src/wallet.py



clean:
	rm -rf all