angular
    .module('loteria')
    .controller('DiaSorteV2Controller', DiaSorteController);

function DiaSorteController(diaSorteService) {
    let vm = this;

    //Funcoes
    vm.iniciar = iniciar;
    vm.limparTudo = limparTudo;
    vm.limparDezenas = limparDezenas;
    vm.sortear = sortear;
    vm.alteraDezena = alteraDezena;

    //Variaveis
    vm.resultado = '';
    vm.dezenas = [];
    vm.quant_dezenas_01_10 = "0";
    vm.quant_dezenas_11_20 = "0";
    vm.quant_dezenas_21_31 = "0";
    vm.quantidade_jogos = "5";
    vm.mensagemErro = [];

    //Variaveis internas

    //Implementacao de funcoes
    function iniciar(){
        for(let i = 1; i <= 31; i ++){
            let dezena = diaSorteService.montaDezena(i);
            vm.dezenas.push(dezena);
        }
    }

    function alteraDezena(indice){
        let qtdFixo = 0;
        for(let i in vm.dezenas){
            if(vm.dezenas[i].estado === 1){
                qtdFixo++;
            }
        }

        console.log(qtdFixo);

        if(qtdFixo < 3){
            vm.dezenas[indice].estado = 1;
            diaSorteService.alteraClasseDezena(vm.dezenas[indice]);
        }
    }

    // function limpaSelecao(dezena){
    //     dezena.estado = 0;
    //     alteraClasse(dezena);
    // }
    //
    // function selecionaFixo(dezena){
    //     var existeFixo = false;
    //     for(i in vm.dezenas){
    //         if(vm.dezenas[i].estado === 1){
    //             existeFixo = true;
    //             break;
    //         }
    //     }
    //
    //     if(!existeFixo){
    //         dezena.estado = 1;
    //         alteraClasse(dezena);
    //     }
    //
    // }
    //
    // function selecionaSorteavel(dezena){
    //     var contador = 0;
    //     for(var i in vm.dezenas){
    //         if(vm.dezenas[i].estado === 2){
    //             contador++;
    //         }
    //         if(contador === 10){
    //             break;
    //         }
    //     }
    //
    //     if(contador < 10){
    //         dezena.estado = 2;
    //         alteraClasse(dezena);
    //     }
    // }

    // function trocaSelecao(selecao){
    //     vm.selecaoAtual = selecao;
    // }

    function isQuantidadeCorreta(){
        let total = 0;
        if(vm.quant_dezenas_01_10 !== ""){
            total += parseInt(vm.quant_dezenas_01_10);
        }

        if(vm.quant_dezenas_11_20 !== ""){
            total += parseInt(vm.quant_dezenas_11_20);
        }

        if(vm.quant_dezenas_21_31 !== ""){
            total += parseInt(vm.quant_dezenas_21_31);
        }

        console.log(total);

        if(total !== 7){
            adicionaMensagemErro("A soma das quantidades não pode ser diferente de 7");
            return false;
        }else{
            return true;
        }

    }

    function limparDezenas(){
        for(let i in vm.dezenas){
            vm.dezenas[i].estado = 0;
            diaSorteService.alteraClasseDezena(vm.dezenas[i]);
        }
    }

    function limparTudo(){
        vm.quant_dezenas_01_10 = "0";
        vm.quant_dezenas_11_20 = "0";
        vm.quant_dezenas_21_31 = "0";
        limparDezenas();
    }

    function sortear(){
        limpaMensagemErro();

        if(!isQuantidadeCorreta()){
            return;
        }

        let listaQuantidades =  [];
        listaQuantidades.push(parseInt(vm.quant_dezenas_01_10));
        listaQuantidades.push(parseInt(vm.quant_dezenas_11_20));
        listaQuantidades.push(parseInt(vm.quant_dezenas_21_31));

        let listaFixos = [];
        for(let indice in vm.dezenas){
            let dezena = vm.dezenas[indice];
            if(dezena.estado === 1){
                listaFixos.push(dezena.numero);
            }
        }

        let objetoRequest = diaSorteService.montaObjetoSorteioV2(listaQuantidades, vm.quantidade_jogos, listaFixos);
        diaSorteService.sorteiaJogosV2(objetoRequest, imprimeNaTela);
    }

    function imprimeNaTela(response){
        let resultado = response.data;
        paraTexto(resultado);
    }

    function paraTexto(jogos){
        let texto = '';
        for(let i in jogos){
            for(let j in jogos[i]){
                let numero = jogos[i][j].toString();
                if (numero.length === 1){
                    numero = "0" + numero;
                }
                texto += numero;
                if(j < jogos[i].length -1){
                    texto += ' - ';
                }else{
                    texto += '\n';
                }
            }
        }

        vm.resultado = texto;
    }

    function adicionaMensagemErro(mensagem){
        vm.mensagemErro.push(mensagem);
    }

    function limpaMensagemErro(){
        vm.mensagemErro = [];
    }


}
