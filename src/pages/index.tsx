import React from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';

const lanes = [
  {number: '01', title: 'Understand', text: 'Build the mental models: data, learning, models, retrieval, reasoning, and decision-making.', link: '/docs/foundations/ai-foundations', tone: 'blue'},
  {number: '02', title: 'Build', text: 'Turn ideas into systems with RAG, agents, skills, evaluation, infrastructure, and guardrails.', link: '/docs/knowledge/rag', tone: 'teal'},
  {number: '03', title: 'Question', text: 'Test the claims with failure modes, industry evidence, standards, and thought experiments.', link: '/docs/evidence/industry-voices', tone: 'amber'},
];

const signals = [
  {label: 'RAG', text: 'Retrieval is a quality problem before it is a prompting problem.', link: '/docs/knowledge/rag'},
  {label: 'AGENTS', text: 'A skill is reusable expertise; an agent is the control loop that applies it.', link: '/docs/agents/agents-agentic-skills'},
  {label: 'EVALUATE', text: 'Measure the retriever, the answer, and the decision—not just the demo.', link: '/docs/evaluation/ai-system-evaluation'},
];

export default function Home(): JSX.Element {
  return (
    <Layout title="AI Atlas" description="A living tutorial across the breadth of artificial intelligence">
      <header className={styles.hero}>
        <div className="container">
          <div className={styles.heroGrid}>
            <div className={styles.heroCopy}>
              <div className={styles.kicker}><span className={styles.liveDot} /> Updated through public research and industry signals</div>
              <Heading as="h1" className={styles.title}>Artificial intelligence, mapped as a system.</Heading>
              <p className={styles.subtitle}>
                A visual, evidence-first tutorial across learning, models, RAG, agents, skills, infrastructure, safety, and autonomous systems.
              </p>
              <div className={styles.actions}>
                <Link className="button button--secondary button--lg" to="/docs/intro">Start the tutorial</Link>
                <Link className={styles.textLink} to="/docs/updates">See the daily signal <span>↗</span></Link>
              </div>
              <div className={styles.heroStats}>
                <div><strong>01</strong><span>living map</span></div>
                <div><strong>∞</strong><span>connected ideas</span></div>
                <div><strong>?</strong><span>better questions</span></div>
              </div>
            </div>

            <div className={styles.signal} aria-label="AI Atlas visual map">
              <div className={styles.signalHalo} />
              <div className={`${styles.orbit} ${styles.orbitOne}`} />
              <div className={`${styles.orbit} ${styles.orbitTwo}`} />
              <div className={`${styles.connector} ${styles.connectorTop}`} />
              <div className={`${styles.connector} ${styles.connectorRight}`} />
              <div className={`${styles.connector} ${styles.connectorBottom}`} />
              <div className={`${styles.connector} ${styles.connectorLeft}`} />
              <div className={styles.core}><span className={styles.coreOverline}>THE</span><strong>AI</strong><span>ATLAS</span></div>
              <div className={`${styles.node} ${styles.nodeTop}`}><span>01</span>learn</div>
              <div className={`${styles.node} ${styles.nodeRight}`}><span>02</span>retrieve</div>
              <div className={`${styles.node} ${styles.nodeBottom}`}><span>03</span>act</div>
              <div className={`${styles.node} ${styles.nodeLeft}`}><span>04</span>govern</div>
            </div>
          </div>
        </div>
      </header>

      <main>
        <section className="container" aria-labelledby="method-heading">
          <div className={styles.sectionIntro}>
            <p className={styles.eyebrow}>The method</p>
            <Heading as="h2" id="method-heading">Learn the mechanism. See the system. Challenge the story.</Heading>
          </div>
          <div className={styles.laneGrid}>
            {lanes.map((lane) => (
              <Link className={`${styles.lane} ${styles[`lane${lane.tone}`]}`} to={lane.link} key={lane.number}>
                <span className={styles.laneNumber}>{lane.number}</span>
                <Heading as="h3">{lane.title}</Heading>
                <p>{lane.text}</p>
                <span className={styles.arrow}>Explore the lane <span>→</span></span>
              </Link>
            ))}
          </div>
        </section>

        <section className={styles.signalSection} aria-labelledby="signal-heading">
          <div className="container">
            <div className={styles.sectionIntroRow}>
              <div><p className={styles.eyebrow}>Frontier watch</p><Heading as="h2" id="signal-heading">Signal to watch</Heading></div>
              <Link className={styles.textLinkDark} to="/docs/updates">Open changelog <span>↗</span></Link>
            </div>
            <div className={styles.signalGrid}>
              {signals.map((signal) => (
                <Link className={styles.signalCard} to={signal.link} key={signal.label}>
                  <span className={styles.signalLabel}>{signal.label}</span>
                  <p>{signal.text}</p>
                  <span className={styles.cardArrow}>Read the lens →</span>
                </Link>
              ))}
            </div>
          </div>
        </section>

        <section className="container" aria-labelledby="question-heading">
          <div className={styles.question}>
            <div><p className={styles.eyebrow}>The editorial question</p><Heading as="h2" id="question-heading">What changes when intelligence becomes infrastructure?</Heading></div>
            <p>Every chapter explains the technology, exposes its failure modes, and connects it to public evidence. The goal is not to make AI sound inevitable. It is to make the reasoning visible.</p>
          </div>
        </section>
      </main>
    </Layout>
  );
}
