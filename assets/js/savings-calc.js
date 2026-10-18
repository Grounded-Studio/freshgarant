/* ─────────────────────────────────────────────────────────────────────────
   FreshGarant savings calculator — vanilla JS, no framework.
   Numbers deliberately conservative: Milieu Centraal (~14% household
   waste) + midpoint of tracker-app studies (~50% reduction).

   Expects this HTML scaffold on the page:
     <div class="calc-shell" data-lang="nl|en">
       <div class="calc-inputs">
         <label class="calc-field">
           ...<input type="range" data-calc="weekly" ...>...
           <span data-calc-out="weekly"></span>
         </label>
         <label class="calc-field">
           ...<input type="range" data-calc="waste" ...>...
           <span data-calc-out="waste"></span>
         </label>
       </div>
       <div class="calc-result">
         <span data-calc-out="monthly"></span>  (big number)
         <div data-calc-out="yearly"></div>
         ...bars + co2...
       </div>
     </div>
   See savings.html / nl/savings.html for the real markup.
   ──────────────────────────────────────────────────────────────────────── */
(function () {
  const WASTE_REDUCTION_FACTOR = 0.5;  // midpoint of 30–70% range
  const KG_CO2_PER_KG_WASTE = 2.5;      // EPA / FAO weighted average
  const KG_FOOD_PER_EURO = 1 / 4;       // 1 kg per €4, mixed-basket estimate
  const WEEKS_PER_MONTH = 4.33;

  function fmt(lang, value) {
    const locale = lang === 'nl' ? 'nl-NL' : 'en-GB';
    return new Intl.NumberFormat(locale, {
      style: 'currency',
      currency: 'EUR',
      maximumFractionDigits: 0,
    }).format(Math.round(value));
  }

  function initCalc(shell) {
    const lang = shell.dataset.lang || 'en';
    const weeklyInput = shell.querySelector('[data-calc="weekly"]');
    const wasteInput  = shell.querySelector('[data-calc="waste"]');

    const weeklyOut  = shell.querySelector('[data-calc-out="weekly"]');
    const wasteOut   = shell.querySelector('[data-calc-out="waste"]');
    const monthlyOut = shell.querySelector('[data-calc-out="monthly"]');
    const yearlyOut  = shell.querySelector('[data-calc-out="yearly"]');
    const currentWasteOut = shell.querySelector('[data-calc-out="currentWaste"]');
    const newWasteOut     = shell.querySelector('[data-calc-out="newWaste"]');
    const currentBar      = shell.querySelector('[data-calc-bar="current"]');
    const newBar          = shell.querySelector('[data-calc-bar="new"]');
    const co2Out          = shell.querySelector('[data-calc-out="co2"]');

    function recalc() {
      const weekly = Number(weeklyInput.value);
      const wastePct = Number(wasteInput.value);

      const monthlySpend = weekly * WEEKS_PER_MONTH;
      const currentWaste = monthlySpend * (wastePct / 100);
      const newWaste = currentWaste * (1 - WASTE_REDUCTION_FACTOR);
      const monthlySave = currentWaste - newWaste;
      const yearlySave = monthlySave * 12;
      const yearlyCo2 = Math.round(
        monthlySave * 12 * KG_FOOD_PER_EURO * KG_CO2_PER_KG_WASTE
      );

      if (weeklyOut)  weeklyOut.textContent  = fmt(lang, weekly);
      if (wasteOut)   wasteOut.textContent   = wastePct + '%';
      if (monthlyOut) monthlyOut.textContent = fmt(lang, monthlySave);
      if (yearlyOut)  yearlyOut.textContent  = fmt(lang, yearlySave);
      if (currentWasteOut) currentWasteOut.textContent = fmt(lang, currentWaste);
      if (newWasteOut)     newWasteOut.textContent     = fmt(lang, newWaste);
      if (currentBar) currentBar.style.width = '100%';
      if (newBar)     newBar.style.width     = ((1 - WASTE_REDUCTION_FACTOR) * 100) + '%';
      if (co2Out)     co2Out.textContent     = yearlyCo2;
    }

    weeklyInput.addEventListener('input', recalc);
    wasteInput.addEventListener('input', recalc);
    recalc();  // initial render
  }

  // Boot on DOM ready — supports multiple calculators per page if ever needed.
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }
  ready(function () {
    document.querySelectorAll('.calc-shell[data-lang]').forEach(initCalc);
  });
})();
