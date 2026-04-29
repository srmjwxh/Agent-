from agents import product_manager, developer, tester, documenter

def run_system(task):
    print("User მოთხოვნა:", task)

    pm = product_manager.run(task)
    print("\n[PM]\n", pm)

    dev = developer.run(pm)
    print("\n[DEV]\n", dev)

    test = tester.run(dev)
    print("\n[TEST]\n", test)

    doc = documenter.run(dev)
    print("\n[DOC]\n", doc)

    return pm, dev, test, doc
