import shlex
import subprocess as proc
import filecmp




@given('Server is running on port 4444')
def step_impl(context):
    cmd = "python C:/tests/steps/server7.py"
    process = proc.Popen(shlex.split(cmd), stdout=proc.PIPE, shell=True)
    context.server = process
    context.serverpid = process.pid
    print (process.pid)
   

@when(u'dumper is started with {pathToFile}')
def step_impl(context, pathToFile):
    
    process = proc.Popen(["python", "C:/tests/__main__.py", "-o", pathToFile], stdout=proc.PIPE, stderr=proc.PIPE) 
    out, err = process.communicate()    # execute it, the output goes to the stdout
    exit_code = process.wait() 
    context.exit_code = exit_code
    context.out = out
    context.err = err
    context.path = pathToFile	
	
@then(u'Output is empty')
def step_impl(context):
    assert (context.out == b'')

@then(u'we can kill server')
def step_impl(context):
    #proc.Popen.terminate(context.server)
	proc.call('taskkill /F /T /PID ' + str(context.serverpid))

@then(u'Error is empty')
def step_impl(context):
    print (context.err)
    print (type(context.err))
    assert (context.err== b'')
	
@when(u'dumper is started: {pathToFile} and {port}')
def step_impl(context, pathToFile, port):
    process = proc.Popen(["python", "C:/tests/__main__.py", "-o", pathToFile, "-p", port], stdout=proc.PIPE, stderr=proc.PIPE) 
    out, err = process.communicate()    # execute it, the output goes to the stdout
    exit_code = process.wait() 
    context.exit_code = exit_code
    context.out = out
    context.err = err

@then(u'Refused Error appears')
def step_impl(context):
    print (context.err.decode("utf-8"))
    assert ("ERROR:root:[WinError 10061] No connection could be made because the target machine actively refused it" in (context.err).decode("utf-8"))

@then(u'Exit code is 0')
def step_impl(context):
    assert (context.exit_code == 0)

@then(u'Expected file is created and same with {sample}')
def step_impl(context, sample):
    assert (filecmp.cmp(context.path, sample))