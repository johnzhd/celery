import const


def beebeeto_input_conver(poc_info, task):
    url = task.url()
    if url != None:
        return url

def beebeeto_output(poc_info, poc_ret, task):
    ''' ToDo Check'''
    task.message_push( 'vuln: ' + poc_info['poc']['id'])
    for k,v in poc_ret:
        k = k.lower()
        if k == 'false' or k == 'error':
            continue
        task.message_push(k + ': ' + v + '\n')
    pass

class core:
    def match_work(self, poc_info, task): ## Jump! Jump!
        if task.uri().port not in poc_info['protocol']['port']:
            return False
        if False == task.tag_exists(const.NSTASK_TAG_SERVICE, poc_info['protocol']['name'], const.NSTASK_MATCH_HAS):
            return False
        return True
    def __init__(self, type, task):
        self.bb2 = type(False)
        self.task = task
    def run(self, task, context):
        ### for debug ###
        #print(self.bb2.poc_info)
        #################
        if self.match_work(self.bb2.poc_info, task) == False:
            return False
        options = {}
        options['target'] = task.uri().geturl()
        options['hostname'] = task.uri().hostname
        options['port'] = task.uri().port
        options['verify'] = True
        ### for debug ###
        options['verbose'] = True
        #################
        args = {
            'options': options,
            'success': False,
            'poc_ret': {},
        }
        try:
            args = self.bb2.verify(args)
        except:
            args['success'] = False
        if args['success']:
            ### for debug ###
            '''
            for (k,v) in args['poc_ret'].items:
                print(k,v)
            # '''
            #################
            beebeeto_output(self.bb2.poc_info, args['poc_ret'], task)
            return True
        return False

class shell:
    def __init__(self, type):
        self.type = type
    def RaderCreatePlugin(self, task):
        return core(self.type, task)


def from_beebeeto(mod, name, filename, fullpath):
    ### for debug ###
    """
    print(mod.MyPoc(False).poc_info)
    # """
    #################
    b = hasattr(mod,'MyPoc') and hasattr(mod,'BaseFrame')
    b = b and mod.MyPoc != None and mod.BaseFrame != None 
    if b == False:
        return None
    lambda_shell = shell(mod.MyPoc)
    mod_item = {}
    mod_item['name'] = name
    mod_item['path'] = filename
    mod_item['module'] = lambda_shell
    mod_item['fullpath'] = fullpath
    return mod_item
