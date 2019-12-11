from claimmaker import claim
from flowchart import flowchart
from mousehover import add_mousehover

def main():
    text = claim(flowchart)
    text = add_mousehover(text)
    print(text)

if __name__ == "__main__":
    main()
