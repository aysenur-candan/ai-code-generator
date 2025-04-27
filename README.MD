# AI Code Generator - Docker ve Kubernetes Dağıtımı

Bu proje, yapay zeka destekli bir kod üretme uygulamasını içermektedir. Docker ve Kubernetes kullanılarak yerel ortamda çalıştırılabilir ve dağıtılabilir.

## İçindekiler

1. [Başlangıç](#başlangıç)
2. [Teknik Gereksinimler](#teknik-gereksinimler)
3. [Kurulum ve Çalıştırma](#kurulum-ve-çalıştırma)
    - [Docker ile Çalıştırma](#docker-ile-çalıştırma)
    - [Kubernetes ile Çalıştırma](#kubernetes-ile-çalıştırma)
4. [Helm Chart Kullanımı](#helm-chart-kullanımı)
5. [Proje Yapısı](#proje-yapısı)

---

## Başlangıç

Bu proje, bir **AI Code Generator** uygulaması içeriyor ve Docker ile paketlenmiştir. Uygulamanın amacı, kullanıcı tarafından sağlanan bazı girdilere dayanarak otomatik olarak kod üretmektir. Kubernetes üzerinde dağıtım yapılabilir.

### Projeyi Çalıştırmak İçin:

- Docker'ı ve Kubernetes'i kurarak yerel ortamda çalıştırabilirsiniz.
- Kubernetes kümesinde dağıtım yapmak için Helm chart kullanabilirsiniz.

---

## Teknik Gereksinimler

- **Docker**: Uygulamayı bir Docker container'ı olarak çalıştırmak için gereklidir.
- **Kubernetes (Minikube veya başka bir küme)**: Uygulamayı Kubernetes kümesine dağıtmak için gereklidir.
- **Helm**: Kubernetes üzerinde uygulama dağıtımını yönetmek için gereklidir.
- **Git**: Projeyi yerel makinenize klonlamak için gereklidir.

---

## Kurulum ve Çalıştırma

### Docker ile Çalıştırma

Uygulamayı Docker container'ında çalıştırmak için şu adımları takip edebilirsiniz:

1. **Dockerfile ile İmajı Oluşturun**

   Projenin kök dizininde aşağıdaki komutu çalıştırarak Docker imajınızı oluşturun:
   
   ```bash
   docker build -t aysenurcandan/ai-code-generator:latest .

### Docker İmajını Çalıştırın

Docker container'ı olarak uygulamanızı başlatmak için şu komutu kullanın:

```bash
docker run -p 5000:5000 aysenurcandan/ai-code-generator:latest

### Kubernetes ile Çalıştırma

Kubernetes üzerinde dağıtım yapmak için aşağıdaki adımları takip edebilirsiniz:

#### Minikube Kümesini Başlatın (Eğer Minikube kullanıyorsanız)

Minikube kümesini başlatmak için şu komutu kullanın:

```bash
minikube start