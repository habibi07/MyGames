### Prosta aplikacja do przechowywania informacji o posiadanych grach

### Aplikacje mozna uruchomić z pomoca docker-compose
```bash
docker-compose up -d --build
```

### Aby uruchomić aplikację lokalnie, trzeba zainstalowac pakiety poleceniem 
```bash
pip install -r requirements.txt
```
oraz uruchomic polecenie
```bash
uvicorn main:app --reload
```

### Testy uruchamia sie poleceniem
```bash
testing=true pytest
```

### Aplikacja działa na porcie 8000

## Końcowe uwagi
 * Można by było jeszcze dodać test stage do dockerfile
 * Do dockerfile dodany jest mongo express do przeglądania bazy, niestety przy pierwszym odpaleniu odrazu sie wywali więc trzeba ręcznie odpalic, to przez to ze usługa mongo startuje później niż kontener, healthcheck jest na to sposobem
