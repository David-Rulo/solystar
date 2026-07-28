import { useState, useEffect, useMemo } from 'react';
import { Search, ShoppingCart, Sun, Zap, Check, Menu, X, Star, TrendingUp, Home, Battery, Shield, Users, ChevronRight, Trash2, Plus, Minus } from 'lucide-react';

const BASE = window.__BACKEND_URL__ || '';
const SLUG = window.__COMPANY_SLUG__ || '';

async function apiFetch(path, opts = {}) {
  const BASE = window.__BACKEND_URL__ || '';
  for (let i = 0; i < 5; i++) {
    try {
      const r = await fetch(BASE + path, opts);
      if (r.ok) return r.json();
    } catch (_) {}
    await new Promise(r => setTimeout(r, 1500));
  }
  return null;
}

function LandingPage() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const style = document.createElement('style');
    style.textContent = `

    `;
    document.head.appendChild(style);
    const handleScroll = () => setScrolled(window.scrollY > 50);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const sections = [
    {
      id: 'inicio',
      title: 'Inicio',
      href: '#inicio'
    },
    {
      id: 'sistemas',
      title: 'Sistemas',
      href: '#sistemas'
    },
    {
      id: 'beneficios',
      title: 'Beneficios',
      href: '#beneficios'
    },
    {
      id: 'precios',
      title: 'Precios',
      href: '#precios'
    },
    {
      id: 'contacto',
      title: 'Contacto',
      href: '#contacto'
    }
  ];

  return (
    <div style={{ minHeight: '100vh', background: '#FFF8F0', fontFamily: "'DM Sans', sans-serif" }}>
      <nav style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        zIndex: 100,
        background: scrolled ? 'rgba(255,248,240,0.95)' : 'transparent',
        backdropFilter: scrolled ? 'blur(12px)' : 'none',
        borderBottom: scrolled ? '1px solid rgba(243,156,18,0.15)' : '1px solid transparent',
        transition: 'all 0.3s ease'
      }}>
        <div style={{ maxWidth: 1280, margin: '0 auto', padding: '16px 24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
            <div style={{ width: 40, height: 40, borderRadius: '50%', background: 'linear-gradient(135deg, #F39C12, #2E86C1)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <Sun size={22} color="#fff" />
            </div>
            <span style={{ fontFamily: "'Poppins', sans-serif", fontSize: 22, fontWeight: 700, color: '#2C3E50' }}>Solystar</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 24 }}>
            {(sections || []).map(s => (
              <a key={s.id} href={s.href} style={{ textDecoration: 'none', color: '#2C3E50', fontSize: 14, fontWeight: 500, transition: 'color 0.2s', opacity: 0.8 }}>{s.title}</a>
            ))}
            <button
              onClick={() => window.location.href = '/auth/login'}
              style={{
                background: 'linear-gradient(135deg, #F39C12, #E67E22)',
                color: '#fff',
                border: 'none',
                padding: '10px 24px',
                borderRadius: 50,
                fontWeight: 600,
                fontSize: 14,
                cursor: 'pointer',
                transition: 'all 0.3s',
                boxShadow: '0 4px 15px rgba(243,156,18,0.3)'
              }}
            >
              Iniciar Sesión
            </button>
          </div>
        </div>
      </nav>

      <section id="inicio" style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', paddingTop: 80, maxWidth: 1280, margin: '0 auto', padding: '120px 24px 80px' }}>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 60, alignItems: 'center' }}>
          <div>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: 8, background: 'rgba(46,134,193,0.1)', padding: '8px 16px', borderRadius: 50, marginBottom: 24 }}>
              <Zap size={18} color="#2E86C1" />
              <span style={{ color: '#2E86C1', fontWeight: 600, fontSize: 14 }}>Energía limpia para tu hogar</span>
            </div>
            <h1 style={{
              fontFamily: "'Poppins', sans-serif",
              fontSize: 52,
              fontWeight: 800,
              color: '#2C3E50',
              lineHeight: 1.2,
              margin: '0 0 20px'
            }}>
              Energía solar con baterías para hogares en Centroamérica
            </h1>
            <p style={{ fontSize: 18, color: '#5D6D7E', lineHeight: 1.6, marginBottom: 32 }}>
              Hasta un <strong style={{ color: '#F39C12' }}>40% de ahorro</strong> en tu factura eléctrica con nuestros sistemas fotovoltaicos con almacenamiento. Energía confiable para tu hogar.
            </p>
            <div style={{ display: 'flex', gap: 16, marginBottom: 40 }}>
              <button
                onClick={() => window.location.href = '/auth/signup'}
                style={{
                  background: 'linear-gradient(135deg, #F39C12, #E67E22)',
                  color: '#fff',
                  border: 'none',
                  padding: '16px 36px',
                  borderRadius: 50,
                  fontWeight: 700,
                  fontSize: 16,
                  cursor: 'pointer',
                  transition: 'all 0.3s',
                  boxShadow: '0 4px 20px rgba(243,156,18,0.4)'
                }}
              >
                Cotiza tu sistema gratis
              </button>
              <button
                onClick={() => window.location.href = '#sistemas'}
                style={{
                  background: 'transparent',
                  color: '#2E86C1',
                  border: '2px solid #2E86C1',
                  padding: '14px 36px',
                  borderRadius: 50,
                  fontWeight: 600,
                  fontSize: 16,
                  cursor: 'pointer',
                  transition: 'all 0.3s'
                }}
              >
                Ver sistemas
              </button>
            </div>
            <div style={{ display: 'flex', gap: 40 }}>
              <div>
                <div style={{ fontFamily: "'Poppins', sans-serif", fontSize: 32, fontWeight: 700, color: '#F39C12' }}>40%</div>
                <div style={{ color: '#5D6D7E', fontSize: 14 }}>Ahorro en factura</div>
              </div>
              <div>
                <div style={{ fontFamily: "'Poppins', sans-serif", fontSize: 32, fontWeight: 700, color: '#F39C12' }}>500+</div>
                <div style={{ color: '#5D6D7E', fontSize: 14 }}>Hogares instalados</div>
              </div>
              <div>
                <div style={{ fontFamily: "'Poppins', sans-serif", fontSize: 32, fontWeight: 700, color: '#F39C12' }}>5 años</div>
                <div style={{ color: '#5D6D7E', fontSize: 14 }}>Garantía baterías</div>
              </div>
            </div>
          </div>
          <div style={{ background: 'linear-gradient(135deg, rgba(243,156,18,0.1), rgba(46,134,193,0.1))', borderRadius: 30, padding: 40, textAlign: 'center' }}>
            <div style={{ width: 120, height: 120, borderRadius: '50%', background: 'linear-gradient(135deg, #F39C12, #2E86C1)', margin: '0 auto 20px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <Sun size={60} color="#fff" />
            </div>
            <h3 style={{ fontFamily: "'Poppins', sans-serif", fontSize: 20, color: '#2C3E50', marginBottom: 12 }}>Sistema Solar con Baterías</h3>
            <p style={{ color: '#5D6D7E', fontSize: 15, lineHeight: 1.5, marginBottom: 20 }}>
              Almacena energía para usarla de noche o durante cortes eléctricos. Independencia energética real para tu hogar.
            </p>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 16 }}>
              <div style={{ background: '#fff', borderRadius: 16, padding: 16, boxShadow: '0 4px 12px rgba(0,0,0,0.05)' }}>
                <Battery size={24} color="#F39C12" />
                <div style={{ fontSize: 13, color: '#2C3E50', marginTop: 8, fontWeight: 600 }}>Baterías LiFePO4</div>
              </div>
              <div style={{ background: '#fff', borderRadius: 16, padding: 16, boxShadow: '0 4px 12px rgba(0,0,0,0.05)' }}>
                <Zap size={24} color="#F39C12" />
                <div style={{ fontSize: 13, color: '#2C3E50', marginTop: 8, fontWeight: 600 }}>Inversor Híbrido</div>
              </div>
              <div style={{ background: '#fff', borderRadius: 16, padding: 16, boxShadow: '0 4px 12px rgba(0,0,0,0.05)' }}>
                <Shield size={24} color="#F39C12" />
                <div style={{ fontSize: 13, color: '#2C3E50', marginTop: 8, fontWeight: 600 }}>Monitoreo App</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="sistemas" style={{ background: '#FFF', padding: '100px 24px' }}>
        <div style={{ maxWidth: 1280, margin: '0 auto' }}>
          <div style={{ textAlign: 'center', marginBottom: 60 }}>
            <h2 style={{ fontFamily: "'Poppins', sans-serif", fontSize: 36, fontWeight: 700, color: '#2C3E50', marginBottom: 16 }}>
              Nuestros Sistemas Solares
            </h2>
            <p style={{ color: '#5D6D7E', fontSize: 17, maxWidth: 600, margin: '0 auto' }}>
              Soluciones completas con paneles solares, baterías de litio e inversores híbridos para hogares centroamericanos.
            </p>
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 32 }}>
            {[
              { name: 'Solystar Básico 3kW', price: '$2,990', desc: 'Para hogares pequeños (1-2 personas). Reduce hasta 30% tu factura.', features: ['3 paneles 450W', 'Batería 5kWh', 'Inversor 3kW', 'Instalación básica'] },
              { name: 'Solystar Estándar 5kW', price: '$4,990', desc: 'Para familias de 3-4 personas. Ahorro garantizado del 40%.', features: ['5 paneles 450W', 'Batería 10kWh', 'Inversor 5kW', 'Monitoreo remoto'] },
              { name: 'Solystar Premium 8kW', price: '$7,990', desc: 'Para hogares grandes. Independencia energética total.', features: ['8 paneles 450W', 'Batería 15kWh', 'Inversor 8kW', 'App + Soporte VIP'] }
            ].map((sistema, i) => (
              <div key={i} style={{
                background: '#FFF8F0',
                borderRadius: 24,
                padding: 32,
                border: '1px solid rgba(243,156,18,0.15)',
                transition: 'all 0.3s',
                position: 'relative',
                overflow: 'hidden'
              }}>
                {i === 1 && (
                  <div style={{ background: '#F39C12', color: '#fff', padding: '6px 16px', borderRadius: '0 0 12px 12px', position: 'absolute', top: 0, right: 24, fontSize: 12, fontWeight: 700 }}>
                    MÁS POPULAR
                  </div>
                )}
                <div style={{ width: 48, height: 48, borderRadius: 12, background: 'linear-gradient(135deg, #F39C12, #E67E22)', display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: 20 }}>
                  <Sun size={24} color="#fff" />
                </div>
                <h3 style={{ fontFamily: "'Poppins', sans-serif", fontSize: 20, fontWeight: 700, color: '#2C3E50', marginBottom: 8 }}>{sistema.name}</h3>
                <p style={{ color: '#5D6D7E', fontSize: 14, marginBottom: 16 }}>{sistema.desc}</p>
                <div style={{ fontFamily: "'Poppins', sans-serif", fontSize: 28, fontWeight: 700, color: '#F39C12', marginBottom: 20 }}>
                  {sistema.price}
                  <span style={{ fontSize: 14, color: '#5D6D7E', fontWeight: 400 }}> / instalado</span>
                </div>
                <ul style={{ listStyle: 'none', padding: 0, margin: '0 0 24px' }}>
                  {sistema.features.map((f, j) => (
                    <li key={j} style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 10, color: '#2C3E50', fontSize: 14 }}>
                      <Check size={16} color="#2E86C1" />
                      {f}
                    </li>
                  ))}
                </ul>
                <button
                  onClick={() => window.location.href = '/auth/signup'}
                  style={{
                    width: '100%',
                    padding: 14,
                    background: i === 1 ? 'linear-gradient(135deg, #F39C12, #E67E22)' : 'transparent',
                    color: i === 1 ? '#fff' : '#F39C12',
                    border: i === 1 ? 'none' : '2px solid #F39C12',
                    borderRadius: 12,
                    fontWeight: 600,
                    fontSize: 15,
                    cursor: 'pointer',
                    transition: 'all 0.3s'
                  }}
                >
                  Cotizar ahora
                </button>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="beneficios" style={{ padding: '100px 24px', maxWidth: 1280, margin: '0 auto' }}>
        <div style={{ textAlign: 'center', marginBottom: 60 }}>
          <h2 style={{ fontFamily: "'Poppins', sans-serif", fontSize: 36, fontWeight: 700, color: '#2C3E50', marginBottom: 16 }}>
            ¿Por qué elegir Solystar?
          </h2>
          <p style={{ color: '#5D6D7E', fontSize: 17, maxWidth: 600, margin: '0 auto' }}>
            La mejor relación calidad-precio en energía solar para hogares centroamericanos.
          </p>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: 32 }}>
          {[
            { icon: <Zap size={32} />, title: 'Ahorro Real', desc: 'Hasta 40% de reducción en tu factura eléctrica desde el primer mes.' },
            { icon: <Battery size={32} />, title: 'Baterías Incluidas', desc: 'Almacena energía para la noche y cortes eléctricos. Libertad energética.' },
            { icon: <Home size={32} />, title: 'Instalación Rápida', desc: 'Instalamos tu sistema en 1-2 días. Sin obras ni complicaciones.' },
            { icon: <Shield size={32} />, title: '5 Años de Garantía', desc: 'Baterías LiFePO4 con 5 años de garantía y soporte local.' },
            { icon: <Users size={32} />, title: 'Soporte en Español', desc: 'Equipo de soporte local para toda Centroamérica. Siempre disponibles.' },
            { icon: <TrendingUp size={32} />, title: 'Financiamiento', desc: 'Planes de pago flexibles. Tu sistema se paga solo con el ahorro.' }
          ].map((b, i) => (
            <div key={i} style={{
              background: '#FFF',
              borderRadius: 20,
              padding: 28,
              border: '1px solid rgba(243,156,18,0.1)',
              transition: 'all 0.3s',
              textAlign: 'center'
            }}>
              <div style={{ color: '#F39C12', marginBottom: 16 }}>{b.icon}</div>
              <h3 style={{ fontFamily: "'Poppins', sans-serif", fontSize: 18, fontWeight: 600, color: '#2C3E50', marginBottom: 8 }}>{b.title}</h3>
              <p style={{ color: '#5D6D7E', fontSize: 14, lineHeight: 1.5 }}>{b.desc}</p>
            </div>
          ))}
        </div>
      </section>

      <section style={{ background: '#2C3E50', padding: '80px 24px', color: '#fff', textAlign: 'center' }}>
        <div style={{ maxWidth: 700, margin: '0 auto' }}>
          <h2 style={{ fontFamily: "'Poppins', sans-serif", fontSize: 32, fontWeight: 700, marginBottom: 16 }}>
            Más de 500 hogares centroamericanos ya ahorran con Solystar
          </h2>
          <p style={{ color: '#95A5A6', fontSize: 16, marginBottom: 32 }}>
            Únete a la revolución solar. Cotiza tu sistema hoy y empieza a ahorrar desde tu primera factura.
          </p>
          <div style={{ display: 'flex', gap: 40, justifyContent: 'center', marginBottom: 40 }}>
            <div>
              <div style={{ fontFamily: "'Poppins', sans-serif", fontSize: 36, fontWeight: 700, color: '#F39C12' }}>40%</div>
              <div style={{ color: '#95A5A6', fontSize: 14 }}>Ahorro promedio</div>
            </div>
            <div>
              <div style={{ fontFamily: "'Poppins', sans-serif", fontSize: 36, fontWeight: 700, color: '#F39C12' }}>500+</div>
              <div style={{ color: '#95A5A6', fontSize: 14 }}>Hogares instalados</div>
            </div>
            <div>
              <div style={{ fontFamily: "'Poppins', sans-serif", fontSize: 36, fontWeight: 700, color: '#F39C12' }}>98%</div>
              <div style={{ color: '#95A5A6', fontSize: 14 }}>Satisfacción</div>
            </div>
          </div>
          <button
            onClick={() => window.location.href = '/auth/signup'}
            style={{
              background: 'linear-gradient(135deg, #F39C12, #E67E22)',
              color: '#fff',
              border: 'none',
              padding: '16px 40px',
              borderRadius: 50,
              fontWeight: 700,
              fontSize: 16,
              cursor: 'pointer',
              boxShadow: '0 4px 20px rgba(243,156,18,0.4)'
            }}
          >
            Cotiza tu sistema gratis
          </button>
        </div>
      </section>

      <section id="precios" style={{ padding: '100px 24px', maxWidth: 1280, margin: '0 auto' }}>
        <div style={{ textAlign: 'center', marginBottom: 60 }}>
          <h2 style={{ fontFamily: "'Poppins', sans-serif", fontSize: 36, fontWeight: 700, color: '#2C3E50', marginBottom: 16 }}>
            Planes para tu hogar
          </h2>
          <p style={{ color: '#5D6D7E', fontSize: 17, maxWidth: 600, margin: '0 auto' }}>
            Elige el plan que mejor se adapte a tus necesidades. Todos incluyen instalación y garantía.
          </p>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: 32 }}>
          {[
            { name: 'Básico', price: '$0', desc: 'Cotización gratuita y catálogo completo', features: ['Catálogo de sistemas', 'Cotización sin compromiso', 'Asesoría básica por email', 'Guía de instalación'] },
            { name: 'Premium', price: '$49/mes', desc: 'Cotizaciones ilimitadas y soporte prioritario', popular: true, features: ['Todo lo del plan Básico', 'Cotizaciones ilimitadas', 'Soporte prioritario 24/7', 'Monitoreo en tiempo real', 'Descuentos en equipos'] },
            { name: 'Empresarial', price: '$199/mes', desc: 'API, integraciones y equipo dedicado', features: ['Todo lo del plan Premium', 'API de cotización', 'Integraciones ERP', 'Equipo dedicado', 'Reportes avanzados', 'SLA garantizado'] }
          ].map((plan, i) => (
            <div key={i} style={{
              background: '#FFF',
              borderRadius: 24,
              padding: 32,
              border: plan.popular ? '2px solid #F39C12' : '1px solid rgba(0,0,0,0.08)',
              position: 'relative',
              transition: 'all 0.3s'
            }}>
              {plan.popular && (
                <div style={{ background: '#F39C12', color: '#fff', padding: '6px 16px', borderRadius: '0 0 12px 12px', position: 'absolute', top: 0, right: 24, fontSize: 12, fontWeight: 700 }}>
                  RECOMENDADO
                </div>
              )}
              <h3 style={{ fontFamily: "'Poppins', sans-serif", fontSize: 20, fontWeight: 700, color: '#2C3E50', marginBottom: 8 }}>{plan.name}</h3>
              <p style={{ color: '#5D6D7E', fontSize: 14, marginBottom: 16 }}>{plan.desc}</p>
              <div style={{ fontFamily: "'Poppins', sans-serif", fontSize: 28, fontWeight: 700, color: '#F39C12', marginBottom: 24 }}>
                {plan.price}
              </div>
              <ul style={{ listStyle: 'none', padding: 0, margin: '0 0 24px' }}>
                {plan.features.map((f, j) => (
                  <li key={j} style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 10, color: '#2C3E50', fontSize: 14 }}>
                    <Check size={16} color="#2E86C1" />
                    {f}
                  </li>
                ))}
              </ul>
              <button
                onClick={() => window.location.href = '/auth/signup'}
                style={{
                  width: '100%',
                  padding: 14,
                  background: plan.popular ? 'linear-gradient(135deg, #F39C12, #E67E22)' : 'transparent',
                  color: plan.popular ? '#fff' : '#F39C12',
                  border: plan.popular ? 'none' : '2px solid #F39C12',
                  borderRadius: 12,
                  fontWeight: 600,
                  fontSize: 15,
                  cursor: 'pointer',
                  transition: 'all 0.3s'
                }}
              >
                Elegir plan
              </button>
            </div>
          ))}
        </div>
      </section>

      <section id="contacto" style={{ background: '#FFF', padding: '80px 24px' }}>
        <div style={{ maxWidth: 600, margin: '0 auto', textAlign: 'center' }}>
          <h2 style={{ fontFamily: "'Poppins', sans-serif", fontSize: 32, fontWeight: 700, color: '#2C3E50', marginBottom: 16 }}>
            ¿Listo para ahorrar hasta 40%?
          </h2>
          <p style={{ color: '#5D6D7E', fontSize: 16, marginBottom: 32 }}>
            Déjanos tus datos y un asesor te contactará en menos de 24 horas. ¡Sin compromiso!
          </p>
          <form style={{ display: 'flex', flexDirection: 'column', gap: 12 }} onSubmit={e => { e.preventDefault(); window.location.href = '/auth/signup'; }}>
            <input placeholder="Tu nombre completo" style={{ padding: 14, borderRadius: 12, border: '1px solid rgba(0,0,0,0.1)', fontSize: 15, outline: 'none' }} />
            <input type="email" placeholder="tu@email.com" style={{ padding: 14, borderRadius: 12, border: '1px solid rgba(0,0,0,0.1)', fontSize: 15, outline: 'none' }} />
            <select style={{ padding: 14, borderRadius: 12, border: '1px solid rgba(0,0,0,0.1)', fontSize: 15, outline: 'none', background: '#FFF' }}>
              <option>País</option>
              <option>Guatemala</option>
              <option>El Salvador</option>
              <option>Honduras</option>
              <option>Nicaragua</option>
              <option>Costa Rica</option>
              <option>Panamá</option>
            </select>
            <textarea placeholder="Cuéntanos sobre tu hogar..." rows={3} style={{ padding: 14, borderRadius: 12, border: '1px solid rgba(0,0,0,0.1)', fontSize: 15, outline: 'none', resize: 'vertical' }} />
            <button type="submit" style={{ padding: 16, background: 'linear-gradient(135deg, #F39C12, #E67E22)', color: '#fff', border: 'none', borderRadius: 12, fontWeight: 700, fontSize: 16, cursor: 'pointer' }}>
              Solicitar cotización gratuita
            </button>
          </form>
        </div>
      </section>

      <footer style={{ background: '#2C3E50', color: '#95A5A6', padding: '60px 24px 30px' }}>
        <div style={{ maxWidth: 1280, margin: '0 auto', display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 40 }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 16 }}>
              <div style={{ width: 36, height: 36, borderRadius: '50%', background: 'linear-gradient(135deg, #F39C12, #2E86C1)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                <Sun size={18} color="#fff" />
              </div>
              <span style={{ fontFamily: "'Poppins', sans-serif", fontSize: 18, fontWeight: 700, color: '#fff' }}>Solystar</span>
            </div>
            <p style={{ fontSize: 14, lineHeight: 1.6 }}>Energía solar con baterías para hogares en Centroamérica. Hasta 40% de ahorro en tu factura eléctrica.</p>
          </div>
          <div>
            <h4 style={{ color: '#fff', fontFamily: "'Poppins', sans-serif", fontSize: 15, fontWeight: 600, marginBottom: 16 }}>Productos</h4>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8, fontSize: 14 }}>
              <span>Sistemas 3kW</span>
              <span>Sistemas 5kW</span>
              <span>Sistemas 8kW</span>
              <span>Baterías LiFePO4</span>
            </div>
          </div>
          <div>
            <h4 style={{ color: '#fff', fontFamily: "'Poppins', sans-serif", fontSize: 15, fontWeight: 600, marginBottom: 16 }}>Empresa</h4>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8, fontSize: 14 }}>
              <span>Sobre nosotros</span>
              <span>Casos de éxito</span>
              <span>Blog</span>
              <span>Contacto</span>
            </div>
          </div>
          <div>
            <h4 style={{ color: '#fff', fontFamily: "'Poppins', sans-serif", fontSize: 15, fontWeight: 600, marginBottom: 16 }}>Soporte</h4>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8, fontSize: 14 }}>
              <span>Centro de ayuda</span>
              <span>Garantía</span>
              <span>Financiamiento</span>
              <span>WhatsApp</span>
            </div>
          </div>
        </div>
        <div style={{ maxWidth: 1280, margin: '40px auto 0', paddingTop: 24, borderTop: '1px solid rgba(255,255,255,0.1)', textAlign: 'center', fontSize: 14 }}>
          © 2024 Solystar. Todos los derechos reservados. Energía que transforma hogares.
        </div>
      </footer>
    </div>
  );
}

function ProductApp({ user, onLogout }) {
  /* NC_PLACEHOLDER_DASHBOARD — replaced by the real dashboard in Phase 2 */
  return (
    <div style={{ minHeight: '100vh', background: '#0a0d18', color: '#e6eaf2', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 16, padding: 24, textAlign: 'center' }}>
      <h1 style={{ fontSize: 28, fontWeight: 800, margin: 0 }}>Welcome, {user?.name || user?.email || 'there'} 👋</h1>
      <p style={{ color: '#9aa6bd', maxWidth: 460, lineHeight: 1.5, margin: 0 }}>Your account is ready. Your dashboard is being set up and will appear here shortly.</p>
      <button onClick={onLogout} style={{ marginTop: 8, padding: '10px 18px', borderRadius: 10, border: '1px solid #2a3350', background: 'transparent', color: '#e6eaf2', fontWeight: 600, cursor: 'pointer' }}>Log out</button>
    </div>
  );
}

function AuthGate({ onAuth, onClose }) {
  const [mode, setMode] = useState('signup');
  const [form, setForm] = useState({ name: '', email: '', password: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const _ip = { width: '100%', padding: '11px 13px', margin: '6px 0', borderRadius: 9, border: '1px solid #2a3350', background: '#0b1020', color: '#e6eaf2', fontSize: 14, outline: 'none', boxSizing: 'border-box' };
  const submit = async (e) => {
    e.preventDefault();
    if (!form.email || !form.password) return;
    setLoading(true); setError('');
    const _b = window.__NC_BASE__ || ''; const _s = window.__COMPANY_SLUG__ || '';
    const body = JSON.stringify({ email: form.email, password: form.password, name: form.name });
    const _call = () => fetch(`${_b}/api/c/${_s}/auth/${mode}`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body });
    try {
      let res; try { res = await _call(); } catch { await new Promise(r => setTimeout(r, 2500)); res = await _call(); }
      const json = await res.json();
      if (!json.ok) { setError(json.error || 'Authentication failed — please try again'); setLoading(false); return; }
      onAuth(json);
    } catch { setError('Connection error — please try again in a moment.'); setLoading(false); }
  };
  return (
    <div onClick={onClose} style={{ position: 'fixed', inset: 0, background: 'rgba(2,6,18,.7)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000 }}>
      <form onClick={(e) => e.stopPropagation()} onSubmit={submit} style={{ background: '#0f1424', border: '1px solid #232b45', padding: 28, borderRadius: 16, width: 360, maxWidth: '90vw', color: '#e6eaf2' }}>
        <h3 style={{ margin: '0 0 16px', fontSize: 20, fontWeight: 700 }}>{mode === 'signup' ? 'Create your account' : 'Welcome back'}</h3>
        {mode === 'signup' && <input value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} placeholder="Your name" style={_ip} />}
        <input value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} placeholder="Work email" type="email" required style={_ip} />
        <input value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} placeholder="Password (min 6 chars)" type="password" required style={_ip} />
        {error && <p style={{ color: '#f87171', fontSize: 13, margin: '6px 0 0' }}>{error}</p>}
        <button type="submit" disabled={loading} style={{ width: '100%', marginTop: 10, padding: '12px', borderRadius: 9, border: 'none', background: loading ? '#4b50b8' : '#6366f1', color: '#fff', fontWeight: 700, fontSize: 15, cursor: loading ? 'default' : 'pointer' }}>
          {loading ? '…' : mode === 'signup' ? 'Get started free' : 'Log in'}
        </button>
        <p onClick={() => { setMode(mode === 'signup' ? 'login' : 'signup'); setError(''); }} style={{ marginTop: 14, fontSize: 13, color: '#9aa6bd', cursor: 'pointer', textAlign: 'center' }}>
          {mode === 'signup' ? 'Already have an account? Log in' : 'New here? Create an account'}
        </p>
      </form>
    </div>
  );
}

function App() {
  const [auth, setAuth] = useState(() => {
    try {
      if (localStorage.getItem('nc_user') && !localStorage.getItem('nc_auth')) localStorage.removeItem('nc_user');
      const a = JSON.parse(localStorage.getItem('nc_auth') || 'null');
      return (a && a.token && a.user && typeof a.user.email === 'string') ? a : null;
    } catch { return null; }
  });
  const [showAuth, setShowAuth] = useState(false);
  useEffect(() => {
    if (!auth?.token) return;
    const _b = window.__NC_BASE__ || ''; const _s = window.__COMPANY_SLUG__ || '';
    fetch(`${_b}/api/c/${_s}/auth/me`, { headers: { Authorization: `Bearer ${auth.token}` } })
      .then(r => r.json()).then(d => { if (!d.ok) { localStorage.removeItem('nc_auth'); setAuth(null); } }).catch(() => {});
  }, []);
  const onAuth = (data) => { localStorage.setItem('nc_auth', JSON.stringify(data)); setAuth(data); setShowAuth(false); };
  const onLogout = () => { localStorage.removeItem('nc_auth'); setAuth(null); };
  if (auth?.user) return <ProductApp user={auth.user} token={auth.token} onLogout={onLogout} />;
  return (
    <>
      <LandingPage onGetStarted={() => setShowAuth(true)} onSignup={() => setShowAuth(true)} onLogin={() => setShowAuth(true)} />
      {/* Fallback entry point (bottom-right so it never overlaps the nav) — guarantees a
          working login even if the landing's own buttons aren't wired to the auth modal. */}
      <button onClick={() => setShowAuth(true)} style={{ position: 'fixed', bottom: 20, right: 20, zIndex: 999, background: '#6366f1', color: '#fff', border: 'none', padding: '10px 18px', borderRadius: 999, fontWeight: 600, fontSize: 14, cursor: 'pointer', boxShadow: '0 6px 20px rgba(99,102,241,.45)' }}>Sign in</button>
      {showAuth && <AuthGate onAuth={onAuth} onClose={() => setShowAuth(false)} />}
    </>
  );
}

export default App;
