import { useMemo, useState } from 'react';

/**
 * Interactive savings calculator — pure client-side React island.
 * Numbers are deliberately conservative; we lean on Milieu Centraal
 * (~14% household waste) and the midpoint of tracker-app studies
 * (~50% reduction) rather than top-of-range marketing figures.
 */

type Strings = {
  weeklySpendLabel: string;
  wastePercentLabel: string;
  wasteHint: string;
  resultTitle: string;
  perMonth: string;
  perYear: string;
  co2Saved: string;
  co2Hint: string;
  currentWasteLabel: string;
  newWasteLabel: string;
};

interface Props {
  strings: Strings;
  lang: 'en' | 'nl';
}

// Realistic waste reduction once a user is actively tracking inventory +
// getting expiry reminders. Studies range 30–70%; we take the midpoint.
const WASTE_REDUCTION_FACTOR = 0.5;

// EPA / FAO consensus: ~2.5 kg CO₂-eq per kg of food waste averaged across
// categories. Lower bound stays honest.
const KG_CO2_PER_KG_WASTE = 2.5;

// Approximate kg of food per euro spent (varies hugely by product type —
// 1 kg bread ≠ 1 kg steak in price). 1 kg per €4 is a weighted guess for
// a typical mixed shopping basket.
const KG_FOOD_PER_EURO = 1 / 4;

const WEEKS_PER_MONTH = 4.33;

function format(lang: 'en' | 'nl', value: number): string {
  const locale = lang === 'nl' ? 'nl-NL' : 'en-GB';
  return new Intl.NumberFormat(locale, {
    style: 'currency',
    currency: 'EUR',
    maximumFractionDigits: 0,
  }).format(Math.round(value));
}

export default function SavingsCalc({ strings, lang }: Props) {
  const [weeklySpend, setWeeklySpend] = useState(80);
  const [wastePct, setWastePct] = useState(14);

  const calc = useMemo(() => {
    const monthlySpend = weeklySpend * WEEKS_PER_MONTH;
    const currentMonthlyWaste = monthlySpend * (wastePct / 100);
    const newMonthlyWaste = currentMonthlyWaste * (1 - WASTE_REDUCTION_FACTOR);
    const monthlySavings = currentMonthlyWaste - newMonthlyWaste;
    const yearlySavings = monthlySavings * 12;
    const yearlyKgSaved =
      monthlySavings * 12 * KG_FOOD_PER_EURO; // kg of food
    const yearlyCo2 = yearlyKgSaved * KG_CO2_PER_KG_WASTE;

    // Width ratios for the bar visual: scale so the "current" bar
    // always fills the available track, "new" shrinks proportionally.
    const currentPct = 100;
    const newPct = (1 - WASTE_REDUCTION_FACTOR) * 100;

    return {
      monthlySavings,
      yearlySavings,
      yearlyCo2: Math.round(yearlyCo2),
      currentMonthlyWaste,
      newMonthlyWaste,
      currentPct,
      newPct,
    };
  }, [weeklySpend, wastePct]);

  return (
    <div className="calc-shell">
      {/* ── Inputs ───────────────────────────────────────────────────── */}
      <div className="calc-inputs">
        <label className="calc-field">
          <span className="calc-field-label">{strings.weeklySpendLabel}</span>
          <span className="calc-field-value">{format(lang, weeklySpend)}</span>
          <input
            type="range"
            min={20}
            max={300}
            step={5}
            value={weeklySpend}
            onChange={(e) => setWeeklySpend(Number(e.target.value))}
            aria-label={strings.weeklySpendLabel}
          />
          <div className="calc-ticks"><span>€20</span><span>€300</span></div>
        </label>

        <label className="calc-field">
          <span className="calc-field-label">{strings.wastePercentLabel}</span>
          <span className="calc-field-value">{wastePct}%</span>
          <input
            type="range"
            min={5}
            max={40}
            step={1}
            value={wastePct}
            onChange={(e) => setWastePct(Number(e.target.value))}
            aria-label={strings.wastePercentLabel}
          />
          <div className="calc-ticks"><span>5%</span><span>40%</span></div>
          <small className="calc-hint">{strings.wasteHint}</small>
        </label>
      </div>

      {/* ── Result ───────────────────────────────────────────────────── */}
      <div className="calc-result">
        <span className="calc-result-kicker">{strings.resultTitle}</span>
        <div className="calc-big-number">
          {format(lang, calc.monthlySavings)}
          <span className="calc-period"> / {strings.perMonth}</span>
        </div>
        <div className="calc-yearly">
          {format(lang, calc.yearlySavings)} <span>{strings.perYear}</span>
        </div>

        {/* Before / after bars */}
        <div className="calc-bars">
          <div className="calc-bar">
            <div className="calc-bar-label">
              <span>{strings.currentWasteLabel}</span>
              <strong>{format(lang, calc.currentMonthlyWaste)}</strong>
            </div>
            <div className="calc-bar-track">
              <div
                className="calc-bar-fill calc-bar-fill-red"
                style={{ width: `${calc.currentPct}%` }}
              />
            </div>
          </div>
          <div className="calc-bar">
            <div className="calc-bar-label">
              <span>{strings.newWasteLabel}</span>
              <strong>{format(lang, calc.newMonthlyWaste)}</strong>
            </div>
            <div className="calc-bar-track">
              <div
                className="calc-bar-fill calc-bar-fill-green"
                style={{ width: `${calc.newPct}%` }}
              />
            </div>
          </div>
        </div>

        <div className="calc-co2">
          <span className="calc-co2-value">{calc.yearlyCo2}</span>
          <span>{strings.co2Saved}</span>
          <small>{strings.co2Hint}</small>
        </div>
      </div>
    </div>
  );
}
