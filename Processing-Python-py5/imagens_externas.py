# Como usar imagens externas

# Acessando um arquivo com `loadImage()`

podemos carregar(_load_) na memória imagens digitais a partir de arquivos externos nos formatos PNG, JPG, GIF, TIF entre outros. para isso usamos a função `load_image()`, mas é preciso indicar onde está o arquivo(o chamado 'caminho completo' do arquivo), ou que ele esteja na pasta `/ data /` dentro da pasta do seu _sketch_(programa).

```
sketch_2020_04a(pasta/folder do sketch)
   L  sketch_2020_04a.pyde(arquivo com o código)
    L  data(pasta/folder)
       L  imagem.jpg(imagem)
```

note que a operação de carregar o arquivo de imagem é relativamente demorada e nunca deve ser executada dentro do laço `draw()`. em geral só precisamos carregar uma vez a imagem e fazemos isso no `setup()`. também é comum criarmos uma variável global que faz referência à imagem, neste exemplo a variável `img`:

```python


def setup():
    size(400, 400)
    global img
    img = load_image("image.jpg")  # arquivo JPG na pasta /data/


def draw():
    # é possível forçar um tamanho com image(imagem, 0, 0, 100, 100)
    image(img, 0, 0)
    # img.width e img.height são as dimensões da imagem original
    # podemos mostrar uma imagem com metade da sua largura e altura originais assim:
    # image(img, 0, 0, img.width / 2, img.height / 2)


```

se a imagem tiver ** exatamente ** a mesma dimensão da área de desenho ela pode ser usada em `background()`.

```python


def setup():
    size(600, 400)
    global imagem_fundo
    # fundo tem que ter exatamente 600x400 pixels
    imagem_fundo = load_image("fundo.png")


def draw():
    background(imagem_fundo)

    # outros desenhos sobre o fundo aqui
```

pode ser conveniente simplesmente usar a função `image()` como visto anteriormente, para desenhar a imagem na área de desenho logo no começo do `draw()`, caso suas dimensões não sejam iguais a área de desenho.

```python


def setup():
    size(600, 400)
    global imagem_fundo
    imagem_fundo = load_image("fundo.png")


def draw():
    # vai forçar/distorcer o tamanho na imagem
    image(imagem_fundo, 0, 0, width, height)

    # ou usamos image(imagem_fundo, 0, 0) mas pode faltar ou sobrar imagem em relação à área.
    # outros desenhos sobre o fundo aqui
```

# Acessando a cor de um pixel da tela ou de uma imagem

use `get()` para os pixels visíveis na tela ou o método `.get()` para os pixels em uma imagem `Py5Image`. como no exemplo abaixo:

```python
   def setup():
        size(500, 500)
        global imagem
        # carregando uma imagem da pasta /data/
        imagem = load_image('arquivo.png')

    def draw():
        iw, ih = imagem.width, imagem.height
        print(iw, ih)
        cor = imagem.get(mouse_x, mouse_y)  # cor do pixel sob o mouse
        fill(cor)
        no_stroke()
        image(imagem, 0, 0)
        circle(mouse_x, mouse_y, 30)
```

# Copiando uma imagem com `copy()`

podemos copiar imagens digitais previamente carregadas na memória para uma região específica da janela de exibição. se a região a ser copiada e a região a ser colada a imagem tiverem tamanhos diferentes, então o conteúdo será automaticamente redimensionado na região de destino.

os parâmetros aceitos pela função `copy()` são:

- `src`: imagem fonte(**opcional**, caso não seja especificada, se refere à própria tela de desenho)
- `sx`: coordenada X do ponto superior esquerdo da região a ser copiada da imagem fonte
- `sy`: coordenada Y do ponto superior esquerdo da região a ser copiada da imagem fonte
- `sw`: largura da região a ser copiada da imagem fonte
- `sh`: altura da região a ser copiada da imagem fonte
- `dx`: coordenada X do ponto superior esquerdo da região de destino na janela
- `dy`: coordenada Y do ponto superior esquerdo da região de destino na janela
- `dw`: largura da região de destino na janela
- `dy`: altura da região de destino na janela

use `copy()` para copiar pixels de uma imagem `Py5Image`, ou de uma região da tela, para outra região da tela.

```python


def setup():
    size(400, 200)
    global imagem
    imagem = load_image('sunflower.png')


def draw():
    image(imagem, 0, 0)
    copy(0, 0, 200, 200, 200, 0, 200, 200)

```

![duas da mesma imagem lado a lado](assets/copy1.png "Duas da mesma imagem lado a lado")

```python


def setup():
    size(200, 200)
    global imagem, imagem2
    imagem = load_image('sunflower.png')
    imagem2 = load_image('sunflower.png')


def draw():
    image(imagem, 0, 0)
    copy(imagem2, 0, 0, 200, 200, 150, 150, 50, 50)

```

![uma imagem externa por cima da janela](assets/copy2.png "Uma imagem externa por cima da janela")

# Assuntos relacionados

- estrutura de pixels das imagens em[pixels e imagens](pixels.md)
- [exportando imagens](exportando_imagem.md)
