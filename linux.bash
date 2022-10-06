N=$1
M=$2
T=$N
K=1
C=$(($M/$N))
F=$(($M%$N))
for (( i=1; i <= 5000; i++ ))
do
sleep $N
mkdir $i
cd $i
> $K.txt
echo $T > $K.txt
echo Новый файл был создан
if [[ $K -eq $C ]]; then
sleep $F
break
fi
K=$(($K+1))
T=$(($T+$N))
done