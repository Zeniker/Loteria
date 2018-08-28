(function(){

    angular
        .module('loteria')
        .service('diaSorteService', diaSorteService);

    function diaSorteService($http){
        var service = {
            sorteiaJogosV1: sorteiaJogosV1,
            montaObjetoSorteioV1: montaObjetoSorteioV1
        };

        function sorteiaJogosV1(escolhasDiaSorte, callback){
            $http({
                method: 'POST',
                data: JSON.stringify(escolhasDiaSorte),
                url: '/jogos/dia_sorte_v1_sorteio'
            }).then(callback, function errorCallback(response) {
                console.log(response);
            });
        }

        function montaObjetoSorteioV1(objeto){
            var objetoSorteio = {}
            objetoSorteio.numero = objeto.numero;
            objetoSorteio.quant_sorteado = 0;
            return objetoSorteio;
        }

        return service;
    }

})();