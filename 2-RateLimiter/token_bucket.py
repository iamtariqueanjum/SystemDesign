import time

class TokenBucket:

    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill_rate = time.time()

    
    def allow_request(self):
        now = time.time()
        elapsed_time = now - self.last_refill_rate

        # refill the tokens
        refill = elapsed_time * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + refill)
        self.last_refill_rate = now

        if self.tokens >= 1:
            print("tokens: ", self.tokens)
            self.tokens -= 1
            return True
        return False
    
bucket = TokenBucket(capacity=5, refill_rate=1) # 1 req/sec

for i in range(10):
    print(i, bucket.allow_request())
    time.sleep(0.4)