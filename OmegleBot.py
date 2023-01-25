from omegle import OmegleClient

oc = OmegleClient()

oc.start_session()

while True:

    # Získání událostí (nové zprávy, ukončení chatu atd.)

    events = oc.get_events()

    for event in events:

        # Kontrola, zda se jedná o novou zprávu

        if event["event"] == "gotMessage":

            # Získání textu zprávy

            message = event["text"]

            print("Partner:", message)

            

            # Zpracování zprávy (např. odpověď na základě klíčových slov)

            if "hello" in message.lower():

                oc.send_message("Hello there!")
