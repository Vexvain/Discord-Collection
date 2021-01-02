import threading
import time
import uuid
import json
import os

class IOManager: ## Manages reading and writing data.
    def __init__(self, file, start=True, jtype=True, binary=False):
        self.Ops = []
        self.Out = {}
        self.Reserved = []

        self.stopthread = False
        self.stopped = True
        self.thread = None
        self.file = file

        if binary:
            self.jtype = False
        else:
            self.jtype = jtype

        self.binary = binary

        if not os.path.isfile(file):
            with open(file, "w+") as file:
                if jtype:
                    file.write("{}")

        if start:
            self.Start()

    def GetId(self):
        return uuid.uuid4()

    def Read(self, waitforwrite=False, id=None):
        if not waitforwrite:
            id = uuid.uuid4()
            self.Ops.append({"type": "r", "wfw": False, "id": id})
        else:
            if id == None:
                return None

            for x in self.Ops:
                if x["id"] == id:
                    return None

            if id in self.Reserved:
                return None

            self.Reserved.append(id)
            self.Ops.append({"type": "r", "wfw": True, "id": id})

        while not id in self.Out:
            time.sleep(.01)

        result = self.Out[id]
        del self.Out[id]
        return result["data"]

    def Write(self, nd, id=None):
        self.Ops.append({"type": "w", "d": nd, "id": id})

    def Start(self):
        if self.stopped:
            self.stopthread = False
            self.thread = threading.Thread(target=self.ThreadFunc)
            self.thread.start()

    def Stop(self):
        if not self.stopthread:
            if not self.stopped:
                self.stopthread = True

    def isStopped(self):
        return self.stopped

    def ThreadFunc(self):
        self.stopped = False
        t = None

        if self.binary:
            t = "b"
        else:
            t = ""

        while not self.stopthread:
            if len(self.Ops) > 0:
                Next = self.Ops[0]
                del self.Ops[0]

                with open(self.file, Next["type"]+t) as file:
                    id = Next["id"]

                    if Next["type"] == "r":
                        if self.jtype:
                            d = json.load(file)
                        else:
                            d = file.read()
                        self.Out[id] = {"data": d, "id": id}

                        if Next["wfw"]:
                            while not self.stopthread:
                                op = None

                                for op in self.Ops:
                                    if op["id"] == id:
                                        break

                                if op == None:
                                    continue

                                self.Reserved.remove(id)
                                self.Ops.remove(op)
                                time.sleep(.01)
                                self.Ops.insert(0, op)
                                break
                            continue

                    elif Next["type"] == "w":
                        if self.jtype:
                            json.dump(Next["d"], file, indent=4)
                        else:
                            file.write(Next["d"])
            else:
                time.sleep(.1)

        self.stopped = True
