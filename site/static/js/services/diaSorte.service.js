(function(){

    angular
        .module('loteria')
        .service('diaSorteService', diaSorteService);

    function diaSorteService($http){
        var service = {
            sorteiaJogosV1: sorteiaJogosV1,
            montaObjetoSorteioV1: montaObjetoSorteioV1,
            sorteiaJogosV2: sorteiaJogosV2,
            montaObjetoSorteioV2: montaObjetoSorteioV2,
            montaDezena: montaDezena,
            alteraClasseDezena: alteraClasseDezena
        };

        function alteraClasseDezena(dezena){
            switch (dezena.estado) {
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

        function montaDezena(numero){
            let dezena = {};
            dezena.numero = numero;
            dezena.estado = 0;
            dezena.quantSorteado = 0;
            dezena.classe = '';

            return dezena;
        }

        function sorteiaJogosV1(escolhasDiaSorte, callback){
            $http({
                method: 'POST',
                data: JSON.stringify(escolhasDiaSorte),
                url: '/jogos/dia_sorte_v1_sorteio'
            }).then(callback, function errorCallback(response) {
                console.log(response);
            });
        }

        function sorteiaJogosV2(objetoDiaSorteV2, callback){
            $http({
                method: 'POST',
                data: JSON.stringify(objetoDiaSorteV2),
                url: '/jogos/dia_sorte_v2_sorteio'
            }).then(callback, function errorCallback(response) {
                console.log(response);
            });
        }

        function montaObjetoSorteioV1(objeto){
            let objetoSorteio = {};
            objetoSorteio.numero = objeto.numero;
            objetoSorteio.quant_sorteado = 0;
            return objetoSorteio;
        }

        function montaObjetoSorteioV2(listaQuantidades, quantidadeJogos, listaFixos, listaExcluidos){
            let objetoSorteio = {};
            objetoSorteio.listaValores = listaQuantidades;
            objetoSorteio.quantidadeJogos = parseInt(quantidadeJogos);
            objetoSorteio.listaFixos = listaFixos;
            objetoSorteio.listaExcluidos = listaExcluidos;
            return objetoSorteio;
        }

        return service;
    }

})();