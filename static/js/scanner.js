/**
 * Scanner Logic - Detecta automáticamente entrada de lector de códigos o teclado
 * Mantiene autofocus en el campo de búsqueda
 */

class BarcodeScannerDetector {
    constructor() {
        this.buffer = '';
        this.isScanning = false;
        this.scanTimeout = null;
        this.lastKeyTime = 0;
        this.keyInterval = 50; // ms entre teclas de un lector (típicamente muy rápido)
        this.minScanLength = 5; // Longitud mínima de un código válido
        this.scanCompleteDelay = 300; // Esperar después de Enter para completar scan
    }

    init() {
        this.setupSearchInput();
        this.setupGlobalKeyListener();
    }

    setupSearchInput() {
        const barcodeInput = document.getElementById('barcode');

        // Autofocus solo al cargar o después de submit en el campo de código
        if (barcodeInput) {
            barcodeInput.focus();
        }

        // Listener para volver a enfocar en barcode solo si presiona Escape en campos de edición
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && document.getElementById('barcode')) {
                document.getElementById('barcode').focus();
            }
        });
    }

    setupGlobalKeyListener() {
        document.addEventListener('keydown', (e) => {
            this.handleKeypress(e);
        });
    }

    handleKeypress(e) {
        // NO procesar si estamos en un prompt/alert/dialog
        if (!document.activeElement || document.activeElement === document.body) {
            return;
        }

        // Si está en un input o textarea normal que NO sea de scan, no procesar
        if ((e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') && 
            e.target.id !== 'searchInput' && e.target.id !== 'adminSearch' && 
            e.target.id !== 'barcode') {
            return;
        }

        // Si está escribiendo en campo de nombre, precio, etc., no procesar
        if (e.target.id === 'name' || e.target.id === 'category' || e.target.id === 'price' ||
            e.target.id === 'changeUsername' || e.target.id === 'changeOldPassword' || 
            e.target.id === 'changeNewPassword' || e.target.id === 'changeNewPasswordConfirm') {
            return;
        }

        // Solo procesar en campos de scan específicos
        if (e.target.id !== 'searchInput' && e.target.id !== 'adminSearch' && 
            e.target.id !== 'barcode') {
            return;
        }

        const currentTime = Date.now();
        const timeSinceLastKey = currentTime - this.lastKeyTime;
        this.lastKeyTime = currentTime;

        // Detectar si es un lector (muchas teclas en poco tiempo)
        if (!this.isScanning && timeSinceLastKey < this.keyInterval && this.buffer.length > 0) {
            this.isScanning = true;
        }

        if (this.isScanning) {
            // En modo scanning
            if (e.key === 'Enter') {
                this.processScan();
                e.preventDefault();
                return;
            } else if (e.key === 'Escape') {
                this.buffer = '';
                this.isScanning = false;
                return;
            }
        }

        // Agregar carácter al buffer si es imprimible
        if (e.key.length === 1 && !e.ctrlKey && !e.altKey && !e.metaKey) {
            this.buffer += e.key;

            // Actualizar solo el input actual (donde está escribiendo)
            e.target.value = this.buffer;

            // Limpiar timeout anterior
            clearTimeout(this.scanTimeout);

            // Si no es scanning y el buffer es muy largo, probablemente sea un lector
            if (!this.isScanning && this.buffer.length > 3) {
                this.scanTimeout = setTimeout(() => {
                    if (this.buffer.length >= this.minScanLength) {
                        this.isScanning = true;
                    }
                }, this.keyInterval * 2);
            }
        }

        if (e.key === 'Enter') {
            if (this.isScanning || this.buffer.length >= this.minScanLength) {
                this.processScan();
                e.preventDefault();
            } else {
                this.processScan();
            }
            this.buffer = '';
            this.isScanning = false;
        }

        if (e.key === 'Escape') {
            this.buffer = '';
            this.isScanning = false;
        }
    }

    processScan() {
        const searchInput = document.getElementById('searchInput') || 
                           document.getElementById('adminSearch');
        
        if (!searchInput || !this.buffer.trim()) {
            this.buffer = '';
            this.isScanning = false;
            return;
        }

        searchInput.value = this.buffer;
        searchInput.focus();

        // Disparar evento de búsqueda
        const event = new Event('input', { bubbles: true });
        searchInput.dispatchEvent(event);

        // Si hay un botón de búsqueda, hacer click
        const searchBtn = document.getElementById('searchBtn');
        if (searchBtn && document.getElementById('searchInput')) {
            setTimeout(() => {
                searchBtn.click();
                this.buffer = '';
                this.isScanning = false;
            }, this.scanCompleteDelay);
        } else {
            this.buffer = '';
            this.isScanning = false;
        }
    }
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    const scanner = new BarcodeScannerDetector();
    scanner.init();

    // Autofocus en el input de búsqueda
    const searchInput = document.getElementById('searchInput') || 
                       document.getElementById('adminSearch') ||
                       document.getElementById('barcode');
    if (searchInput) {
        searchInput.focus();
    }

    // Configurar botón de cámara si existe
    const cameraBtn = document.getElementById('cameraBtn');
    if (cameraBtn) {
        cameraBtn.addEventListener('click', openCameraScanner);
    }
});

// Mantener foco cuando se regresa a la página
document.addEventListener('visibilitychange', () => {
    if (!document.hidden) {
        const searchInput = document.getElementById('searchInput') || 
                           document.getElementById('adminSearch') ||
                           document.getElementById('barcode');
        if (searchInput) {
            searchInput.focus();
        }
    }
});

/**
 * Abre un modal con acceso a cámara para escanear códigos
 */
async function openCameraScanner() {
    // Crear modal HTML
    const modal = document.createElement('div');
    modal.className = 'camera-modal';
    modal.id = 'cameraModal';
    modal.innerHTML = `
        <div class="camera-modal-content">
            <div class="camera-modal-header">
                <h3>📷 Escanear Código de Barras</h3>
                <button type="button" class="close-btn" onclick="closeCameraScanner()">✕</button>
            </div>
            <div class="camera-modal-body">
                <video id="cameraVideo" autoplay playsinline></video>
                <div id="cameraStatus">Iniciando cámara...</div>
                <div id="scanResult"></div>
            </div>
            <div class="camera-modal-footer">
                <p>Coloca el código de barras frente a la cámara</p>
                <button type="button" class="btn-secondary" onclick="closeCameraScanner()">Cerrar</button>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);

    try {
        const video = document.getElementById('cameraVideo');
        const statusDiv = document.getElementById('cameraStatus');
        
        // Solicitar acceso a cámara
        const stream = await navigator.mediaDevices.getUserMedia({
            video: { facingMode: 'environment' }
        });
        
        video.srcObject = stream;
        statusDiv.textContent = 'Cámara lista. Apunta el código...';
        statusDiv.style.color = '#4caf50';

        // Cargar Quagga.js desde CDN
        if (typeof Quagga === 'undefined') {
            loadQuaggaLibrary();
        } else {
            initQuagga(video);
        }

    } catch (error) {
        const statusDiv = document.getElementById('cameraStatus');
        statusDiv.textContent = '❌ No se pudo acceder a la cámara. Usa el lector conectado o escribe manualmente.';
        statusDiv.style.color = '#d32f2f';
        console.error('Error al acceder a cámara:', error);
    }
}

/**
 * Carga la librería Quagga.js desde CDN
 */
function loadQuaggaLibrary() {
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/quagga@0.12.1/dist/quagga.min.js';
    script.onload = () => {
        const video = document.getElementById('cameraVideo');
        if (video && video.srcObject) {
            initQuagga(video);
        }
    };
    script.onerror = () => {
        const statusDiv = document.getElementById('cameraStatus');
        statusDiv.textContent = '⚠️ Error al cargar librería. Intenta con el lector o escribe manualmente.';
        statusDiv.style.color = '#ff9800';
    };
    document.head.appendChild(script);
}

/**
 * Inicializa Quagga para detección de códigos
 */
function initQuagga(videoElement) {
    if (typeof Quagga === 'undefined') return;

    Quagga.init({
        inputStream: {
            name: 'Live',
            type: 'LiveStream',
            target: videoElement,
            constraints: {
                facingMode: 'environment'
            }
        },
        decoder: {
            readers: ['ean_reader', 'ean_8_reader', 'code_128_reader', 'code_39_reader']
        }
    }, (err) => {
        if (err) {
            console.error('Error en Quagga:', err);
            const statusDiv = document.getElementById('cameraStatus');
            statusDiv.textContent = '⚠️ No se pudo inicializar el scanner. Escribe el código manualmente.';
            return;
        }

        Quagga.start();

        // Detectar código encontrado
        Quagga.onDetected((result) => {
            if (result && result.codeResult && result.codeResult.code) {
                const barcode = result.codeResult.code;
                const barcodeInput = document.getElementById('barcode');
                
                if (barcodeInput) {
                    barcodeInput.value = barcode;
                    const resultDiv = document.getElementById('scanResult');
                    if (resultDiv) {
                        resultDiv.innerHTML = `<div style="color: #4caf50; font-weight: bold; margin-top: 10px;">✓ Código detectado: ${barcode}</div>`;
                    }
                    
                    // Cerrar modal después de 1 segundo
                    setTimeout(() => {
                        closeCameraScanner();
                        barcodeInput.focus();
                    }, 1000);
                }
            }
        });
    });
}

/**
 * Cierra el modal de cámara y libera recursos
 */
function closeCameraScanner() {
    // Detener Quagga
    if (typeof Quagga !== 'undefined') {
        try {
            Quagga.stop();
        } catch (e) {}
    }

    // Detener stream de video
    const video = document.getElementById('cameraVideo');
    if (video && video.srcObject) {
        video.srcObject.getTracks().forEach(track => track.stop());
    }

    // Remover modal
    const modal = document.getElementById('cameraModal');
    if (modal) {
        modal.remove();
    }

    // Refocus en barcode
    const barcodeInput = document.getElementById('barcode');
    if (barcodeInput) {
        barcodeInput.focus();
    }
}
