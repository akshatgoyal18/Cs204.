#register is global variable
# PC = PC + 4 at each instruction read
from globalss import *
global register

def addiinst(rs1,immediate):
    return register[rs1] + immediate        # addi instruction

def andiinst(rs1,immediate):
    return register[rs1] & immediate        # andi instruction    


def oriinst(rs1,immediate):
    return register[rs1] | immediate        # immediate instruction


#def ld_inst(rd,rs1,immediate,register,memory_reg):
#    temp = register[rs1] + immediate                # memory_reg -> memory register
#    register[rd] =memory_reg[temp]                # load doubleword  instruction


def lwinst(rs1,immediate):
    if rs1==2:
        return register[rs1] + immediate
    else:
        return register[rs1] + immediate-65536
    

def ldinst(rs1,immediate):        #same as lw_inst 
    if rs1==2:
        return register[rs1] + immediate
    else:
        return register[rs1] + immediate-65536  #65536 == 0x10000000
    
def lhinst(rs1,immediate):
    if rs1==2:
        return register[rs1] + immediate
    else:
        return register[rs1] + immediate-65536
    
def lbinst(rs1,immediate):
    if rs1==2:
        return register[rs1] + immediate
    else:
        return register[rs1] + immediate-65536
    
def jalrinst(rs1,immediate):
    return register[rs1] + immediate
    