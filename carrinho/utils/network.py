import requests

class Network(object):
  """
  Essa classe tem como objetivo tratar da comunicação de dados através da internet e rede
  """
  def request(url, method="GET", params=None):
    """ Função que faz  requests HTTP. Os argumentos passados nessa função são:
    url (string): URL da request.
    method (string): Qual método HTTP será utilizado. São aceitos "GET", "POST", "PUT", "DELETE".
    params (dict): Parâmetros que serão enviados na request. O padrão é nenhum.

    Retorna: Um DICT com a resposta do servidor ou retorna None se passar um método errado
    """
    r = None

    if method == "GET":
      r = requests.get(url, params=params)
    elif method == "POST":
      r = requests.post(url, params=params)
    elif method == "PUT":
      r = requests.put(url, params=params)
    elif method == "DELETE":
      r = requests.delete(url, params=params)
    else:
      return None

    return r.json()
