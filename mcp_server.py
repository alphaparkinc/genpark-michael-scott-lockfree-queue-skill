import sys
import json
from client import MSQueue

def main():
    q = MSQueue()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "enqueue":
            q.enqueue(params.get("val"))
            res = {"status": "ok"}
        elif method == "dequeue":
            val = q.dequeue()
            res = {"val": val}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
