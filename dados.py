# PIB nesse caso é PIB per capita de cada país, não coloquei pib_per_capita pois dificultaria na hora de achar os dados, por isso reduzi apenas para pib


# Link dos dados da População: https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population
# Link dos dados do PIB per capita: https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_PIB_nominal_per_capita
# Link dos dados do IDH: https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_%C3%8Dndice_de_Desenvolvimento_Humano
# Link dos dados da inflação: https://www.dadosmundiais.com/inflacao.php#google_vignette
# Link dos dados do indice Gini: https://pt.countryeconomy.com/demografia/indice-de-gini

from pprint import pprint

dados_paises = {

    "India": {
        "populacao": "1.417.492.000",
        "pib": "2.731",
        "idh": "0,685",
        "inflacao": "4,4%",
        "gini": "25,5"
    },

    "China": {
        "populacao": "1.407.934.000",
        "pib": "13.136",
        "idh": "0,788",
        "inflacao": "0,4%",
        "gini": "35,7"
    },

    "Estados Unidos": {
        "populacao": "342.181.000",
        "pib": "85.373",
        "idh": "0,938",
        "inflacao": "3,0%",
        "gini": "0,40"
    },

    "Indonesia": {
        "populacao": "285.783.000",
        "pib": "5.271",
        "idh": "0,728",
        "inflacao": "2,86%",
        "gini": "0,375"
    },

    "Paquistao": {
        "populacao": "256.204.000",
        "pib": "1.461",
        "idh": "0,544",
        "inflacao": "23,4%",
        "gini": "0,31"
    },

    "Nigeria": {
        "populacao": "236.213.000",
        "pib": "1.110",
        "idh": "0,560",
        "inflacao": "32,5%",
        "gini": "0,35"
    },

    "Brasil": {
        "populacao": "214.244.000",
        "pib": "11.352",
        "idh": "0,786",
        "inflacao": "4,3%",
        "gini": "0,506"
    },

    "Bangladesh": {
        "populacao": "177.567.00",
        "pib": "2.646",
        "idh": "0,685",
        "inflacao": "9,7%",
        "gini": "0,334"
    },

    "Russia": {
        "populacao": "146.022.000",
        "pib": "14.391",
        "idh": "0,832",
        "inflacao": "7,9%",
        "gini": "33,0"
    },

    "Mexico": {
        "populacao": "131.013.000",
        "pib": "15.249",
        "idh": "0,789",
        "inflacao": "4,7%",
        "gini": "0,391"
    },

    "Etiopia": {
        "populacao": "125.092.825",
        "pib": "1.910",
        "idh": "0,522",
        "inflacao": "23,9%",
        "gini": "31,1"
    },

    "Japao": {
        "populacao": "124.127.899",
        "pib": "33.138",
        "idh": "0,925",
        "inflacao": "2,2%",
        "gini": "32,3"
    },

    "Filipinas": {
        "populacao": "109.581.078",
        "pib": "3.485",
        "idh": "0,720",
        "inflacao": "7,92%",
        "gini": "39,3"
    },

    "Republica Democratica do Congo": {
        "populacao": "105.823.799",
        "pib": "1.679",
        "idh": "0,522",
        "inflacao": "17,8%",
        "gini": "44,7"
    },

    "Egito": {
        "populacao": "102.334.404",
        "pib": "3.225",
        "idh": "0,754",
        "inflacao": "33,3%",
        "gini": "28,5"
    },

    "Vietna": {
        "populacao": "97.338.579",
        "pib": "4.623",
        "idh": "0,766",
        "inflacao": "4,1%",
        "gini": "36,1"
    },

    "Turquia": {
        "populacao": "84.339.067",
        "pib": "12.765",
        "idh": "0,799",
        "inflacao": "31,7%",
        "gini": "45,3"
    },

    "Ira": {
        "populacao": "83.992.949",
        "pib": "5.778",
        "idh": "0,799",
        "inflacao": "31,7%",
        "gini": "35,9"
    },

    "Alemanha": {
        "populacao": "83.783.942",
        "pib": "54.291",
        "idh": "0,959",
        "inflacao": "2,4%",
        "gini": "29,4"
    },

    "Tailandia": {
        "populacao": "69.799.978",
        "pib": "7.812",
        "idh": "0,798",
        "inflacao": "0,5%",
        "gini": "33,5"
    },
}

