import pathlib

p = pathlib.Path(r"C:\Users\Plxshie\Desktop\CowFarm\mai.py")
src = p.read_text(encoding="utf-8")

# 1. Add no-response warning in masterTick
old_master = '''  var now = Date.now();

  if(!S.dailySent && now - S.startedAt > 25000){ S.dailySent = true; sendCmd("owo daily"); }'''
new_master = '''  var now = Date.now();

  if(!S._hasOwOResponse && now - S.startedAt > 30000 && !S._warnedNoResponse){
    S._warnedNoResponse = true;
    log("warn", "No OwO response in 30s. Check: 1) OwO bot in this channel? 2) Run 'owo profile' in Discord first 3) Correct channel selected?");
    toast("No OwO response - check channel & OwO setup", "warn");
  }

  if(!S.dailySent && now - S.startedAt > 25000){ S.dailySent = true; sendCmd("owo daily"); }'''
assert old_master in src, "masterTick var now not found"
src = src.replace(old_master, new_master, 1)

# 2. Initialize _hasOwOResponse and _warnedNoResponse in session start
old_session = "    running:true, paused:false, startedAt:Date.now(), dailySent:false, awaitCash:0, lastBalVal:null,"
new_session = "    running:true, paused:false, startedAt:Date.now(), dailySent:false, awaitCash:0, lastBalVal:null, _hasOwOResponse:false, _warnedNoResponse:false,"
assert old_session in src, "session start not found"
src = src.replace(old_session, new_session)

# 3. Add setup hint in step2 subtitle
old_sub = '<p class="stepsub">Pick a server + channel where the OwO bot is active.</p>'
new_sub = '<p class="stepsub">Pick a server + channel where the OwO bot is active. <strong>Make sure you have run `owo profile` in OwO first!</strong></p>'
assert old_sub in src, "step2 subtitle not found"
src = src.replace(old_sub, new_sub)

# 4. Track OwO responses in onMsg (add _hasOwOResponse flag)
old_onmsg = '  if(m.author && m.author.id === OWO_ID && m.channel_id === S.channelId){\n    log("sys", "OwO message received in channel");'
new_onmsg = '  if(m.author && m.author.id === OWO_ID && m.channel_id === S.channelId){\n    S._hasOwOResponse = true;\n    log("sys", "OwO message received in channel");'
assert old_onmsg in src, "onMsg logging not found"
src = src.replace(old_onmsg, new_onmsg, 1)

p.write_text(src, encoding="utf-8")
print("changes applied")
print("lines:", src.count(chr(10)))
