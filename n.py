def split(input_path ,size) :
    num_of_part=int(len(open(input_path,"rb").read())/(size*1024*1024))
    for i in range (num_of_part):
        open(f"part/{i}.bin","wb").write(    open(    input_path ,"rb"  ).read()[i*size*1024*1024: (i+1)*size*1024*1024  ])
    if i :
        open(f"part/{i+1}.bin","wb").write(    open(    input_path ,"rb"  ).read()[ size*1024*1024*num_of_part: len(open(input_path,"rb").read())  ])

def peast(output,part_of_file):
    for i in range(part_of_file):
        open(  output,"ab"  ).write(  open(  f"part/{i}.bin","rb" ) .read() )
# split("a.exe",28)
peast("k.exe",11)
