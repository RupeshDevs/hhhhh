import pathlib

p = pathlib.Path(r"C:\Users\Plxshie\Desktop\CowFarm\mai.py")
src = p.read_text(encoding="utf-8")

# 1. Add a "Test OwO" button after the "Send owo cash now" button
old_btn = '<button class="btn btn-g" id="btn-cashnow"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v10"/></svg>Send owo cash now</button>'
new_btn = old_btn + '\n        <button class="btn btn-g" id="btn-testowo"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9 12l2 2 4-4"/></svg>Test OwO response</button>'
assert old_btn in src, "btn-cashnow not found"
src = src.replace(old_btn, new_btn)

# 2. Add testOwO function before stopFarm
old_stop = "function stopFarm(){"
test_func = '''function testOwO(){
  if(!S.running){ toast("Start a session first.", "warn"); return; }
  toast("Sending 'owo' test command...");
  log("sys", "Testing OwO response in " + S.channelLabel + "...");
  sendCmd("owo", true);
  setTimeout(function(){
    log("sys", "Command sent. Check event log for OwO response. If no response in 10s, OwO may not be in this channel or may be captch-ing you.");
  }, 3000);
}

'''
assert old_stop in src, "stopFarm not found"
src = src.replace(old_stop, test_func + old_stop)

# 3. Wire the button
old_wire = 'document.getElementById("btn-cashnow").addEventListener("click", function(){ sendCmd("owo cash", true); });'
new_wire = old_wire + '\ndocument.getElementById("btn-testowo").addEventListener("click", testOwO);'
assert old_wire in src, "btn-cashnow wire not found"
src = src.replace(old_wire, new_wire)

# 4. Add logging to handleOwO
old_handle = 'function handleOwO(text){\n'
new_handle = 'function handleOwO(text){\n  log("sys", "OwO replied: " + text.slice(0, 200));\n'
assert old_handle in src, "handleOwO not found"
src = src.replace(old_handle, new_handle, 1)

# 5. Add logging to onMsg when OwO message received
old_onmsg = '  if(m.author && m.author.id === OWO_ID && m.channel_id === S.channelId){\n\n    var text = m.content || "";'
new_onmsg = '  if(m.author && m.author.id === OWO_ID && m.channel_id === S.channelId){\n    log("sys", "OwO message received in channel");\n    var text = m.content || "";'
assert old_onmsg in src, "onMsg OwO condition not found"
src = src.replace(old_onmsg, new_onmsg, 1)

p.write_text(src, encoding="utf-8")
print("changes applied")
print("lines:", src.count(chr(10)))
