import fire

def hello(name="World"):
  return "Hi %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)