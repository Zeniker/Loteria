angular
    .module('loteria')
    .controller('DiaSorteController', DiaSorteController);

function DiaSorteController(diaSorteService) {
    var vm = this;

    //Funcoes
    vm.iniciar = iniciar;
    vm.alteraDezena = alteraDezena;
    vm.trocaSelecao = trocaSelecao;
    vm.limparTudo = limparTudo;
    vm.sortear = sortear;

    //Variaveis
    vm.dezenas = [];
    vm.selecaoAtual = -1;
    vm.resultado = '';
    vm.quantidade_jogos = 5;
    vm.mensagemErro = [];

    //Variaveis internas

    //Implementacao de funcoes
    function iniciar(){
        for(var i = 1; i <= 31; i ++){
            var dezena = diaSorteService.montaDezena(i);
            vm.dezenas.push(dezena);
        }
    }

    function alteraDezena(indice){
        switch (vm.selecaoAtual){
            case 0:
                limpaSelecao(vm.dezenas[indice]);
                break;
            case 1:
                selecionaFixo(vm.dezenas[indice]);
                break;
            case 2:
                selecionaSorteavel(vm.dezenas[indice]);
                break;
            default:
                break;
        }
    }

    function alteraClasse(dezena){
        switch (dezena.estado){
            case 1:
                dezena.classe = 'btn-fixo';
                break;
            case 2:
                dezena.classe = 'btn-sorteavel';
                break;
            default:
                dezena.classe = '';
                break;
        }
    }

    function limpaSelecao(dezena){
        dezena.estado = 0;
        alteraClasse(dezena);
    }

    function selecionaFixo(dezena){
        var existeFixo = false;
        for(i in vm.dezenas){
            if(vm.dezenas[i].estado === 1){
                existeFixo = true;
                break;
            }
        }

        if(!existeFixo){
            dezena.estado = 1;
            alteraClasse(dezena);
        }

    }

    function selecionaSorteavel(dezena){
        var contador = 0;
        for(var i in vm.dezenas){
            if(vm.dezenas[i].estado === 2){
                contador++;
            }
            if(contador === 10){
                break;
            }
        }

        if(contador < 10){
            dezena.estado = 2;
            alteraClasse(dezena);
        }
    }

    function trocaSelecao(selecao){
        vm.selecaoAtual = selecao;
    }

    function limparTudo(){
        vm.selecaoAtual = -1;
        for(var i in vm.dezenas){
            vm.dezenas[i].estado = 0;
            alteraClasse(vm.dezenas[i]);
        }
    }

    function sortear(){
        var contadorFixo = 0;
        var contadorSorteavel = 0;
        var dezenaFixa = {};
        var dezenasSorteaveis = [];
        for(var i in vm.dezenas){
            vm.dezenas[i].quantSorteado = 0;
            switch (vm.dezenas[i].estado){
                case 1:
                    contadorFixo++;
                    dezenaFixa = vm.dezenas[i];
                    break;
                case 2:
                    contadorSorteavel++;
                    dezenasSorteaveis.push(vm.dezenas[i]);
                    break;
            }
        }
        vm.mensagemErro = [];

        if(contadorFixo !== 1){
            vm.mensagemErro.push('Selecione uma dezena fixa');
        }

        if(contadorSorteavel !== 10){
            vm.mensagemErro.push('Selecione 10 dezenas sorteaveis');
        }

        if(vm.quantidade_jogos == null || vm.quantidade_jogos % 5 > 0){
            vm.mensagemErro.push('Quantidade de jogos deve ser múltipla de 5');
        }

        if(vm.mensagemErro.length > 0){
            return
        }

        var objetoSorteio = {};
        objetoSorteio.fixo = diaSorteService.montaObjetoSorteioV1(dezenaFixa);
        objetoSorteio.sorteaveis = [];
        objetoSorteio.numero_jogos = parseInt(vm.quantidade_jogos);
        for(i in dezenasSorteaveis){
            objetoSorteio.sorteaveis.push(diaSorteService.montaObjetoSorteioV1(dezenasSorteaveis[i]));
        }
        diaSorteService.sorteiaJogosV1(objetoSorteio, imprimeNaTela);
    }

    function imprimeNaTela(response){
        var resultado = response.data;
        for (var i in resultado){
            resultado[i].sort();
        }
        paraTexto(resultado);
    }

    function paraTexto(jogos){
        var texto = '';
        for(var i in jogos){
            for(var j in jogos[i]){
                texto += jogos[i][j].toString();
                if(j < jogos[i].length -1){
                    texto += ' - ';
                }else{
                    texto += '\n';
                }
            }
        }

        vm.resultado = texto;
    }


}
