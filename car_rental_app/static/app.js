// script simples para evitar múltiplos envios do formulário
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      // encontrar botões de submit no form
      const submits = form.querySelectorAll('button[type="submit"], input[type="submit"]');
      if (!submits.length) return;

      // desabilitar e trocar texto para o primeiro botão
      submits.forEach(function (btn) {
        try {
          btn.disabled = true;
        } catch (err) {}
      });

      const first = submits[0];
      // adicionar spinner e mudar texto
      const spinner = document.createElement('span');
      spinner.className = 'spinner';
      // guarda texto antigo
      const oldText = first.innerHTML;
      first.dataset.oldText = oldText;
      first.innerHTML = '';
      first.appendChild(spinner);
      const text = document.createElement('span');
      text.style.marginLeft = '8px';
      text.textContent = 'Enviando...';
      first.appendChild(text);
    }, { once: true });
  });
});
