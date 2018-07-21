(function(){

    angular
        .module('loteria')
        .service('diaSorteService', diaSorteService);

    function diaSorteService($http){
        var service = {
            sorteiaJogos: sorteiaJogos,
            montaObjetoSorteio: montaObjetoSorteio
        };

        function sorteiaJogos(escolhasDiaSorte, callback){
            $http({
                method: 'POST',
                data: JSON.stringify(escolhasDiaSorte),
                url: '/jogos/dia_sorte_sorteio'
            }).then(callback, function errorCallback(response) {
                console.log(response);
            });
        }

        function montaObjetoSorteio(objeto){
            var objetoSorteio = {}
            objetoSorteio.numero = objeto.numero;
            objetoSorteio.quant_sorteado = 0;
            return objetoSorteio;
        }

        return service;
    }

})();