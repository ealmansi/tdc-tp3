imprimir_comando(){
    local port=$1
    local alpha=$2
    local beta=$3
    local droprate=$4
    local delay=$5
    local delayvar=$6
    echo "echo \"$alpha $beta $droprate $delay $delayvar\" > salida/$port.txt && (sudo ./tp3_server.py $port $droprate $delay $delayvar &) && sleep 3 && (sudo ./tp3_client.py $port $alpha $beta >> salida/$port.txt)"
}

port=5000
for delay in 0.01 0.025
do
    for delayvar in 0.2 0.5
    do
        for droprate in 0.0 0.25 0.5
        do
            for alpha in 0.0 0.125 0.2 0.5 1.0
            do
                if [ ! -f salida/$port.txt ]; then
                    imprimir_comando $port $alpha 0.25 $droprate $delay $delayvar
                fi
                port=$(($port + 1))
            done    
            for beta in 0.0 0.25 0.5 0.75 1.0
            do
                if [ ! -f salida/$port.txt ]; then
                    imprimir_comando $port 0.125 $beta $droprate $delay $delayvar
                fi
                port=$(($port + 1))
            done
        done
    done
done