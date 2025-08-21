Process 60 stopped
* thread #1: tid = 60, 0x00007f527e8f2610, name = 'fhost'
    frame #0:
Process 60 stopped
* thread #8: tid = 60, 0x00007f5281775700 fhost`get(path='/HkP.py') + 27 at fhost.c:139, name = 'fhost/responder', stop reason = invalid address (fault address: 0x30)
    frame #0: {3:#018x} fhost`get(path='/HkP.py') + 27 at fhost.c:139
   136   get(SrvContext *ctx, const char *path)
   137   {
   138       StoredObj *obj = ctx->store->query(shurl_debase(path));
-> 139       switch (obj->type) {
   140           case ObjTypeFile:
   141               ctx->serve_file_id(obj->id);
   142               break;
(lldb) q