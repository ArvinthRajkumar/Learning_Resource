import json, hashlib
def run_card(model, prompt, negative, seed, scheduler, steps, cfg, width, height, lora=None):
    card = dict(model=model, prompt=prompt, negative=negative, seed=seed, scheduler=scheduler, steps=steps, cfg=cfg, size=[width, height], lora=lora)
    card["id"] = hashlib.sha1(json.dumps(card, sort_keys=True).encode()).hexdigest()[:10]       # identical settings give an identical id
    return card
a = run_card("sdxl-base-1.0", "a lighthouse at sunset", "blurry", 1234, "dpmpp_2m_karras", 25, 6.5, 1024, 1024)
b = run_card("sdxl-base-1.0", "a lighthouse at sunset", "blurry", 1234, "dpmpp_2m_karras", 25, 6.5, 1024, 1024)
c = run_card("sdxl-base-1.0", "a lighthouse at sunset", "blurry", 1235, "dpmpp_2m_karras", 25, 6.5, 1024, 1024)
print("same settings -> same id:", a["id"] == b["id"], "| a different seed -> different id:", a["id"] != c["id"])
