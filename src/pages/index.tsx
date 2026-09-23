import React from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';

const features = [
  {title: 'Learn the mechanisms', text: 'Move from first principles to models, retrieval, reasoning, agents, and autonomous systems.', link: '/docs/intro'},
  {title: 'See the trade-offs', text: 'Use diagrams, failure modes, case studies, and thought experiments to test assumptions.', link: '/docs/atlas/roadmap'},
  {title: 'Track the frontier', text: 'Follow public research, industry signals, standards, and emerging practices through daily updates.', link: '/docs/updates'},
];

export default function Home(): JSX.Element {
  return (
    <Layout title="AI Atlas" description="A living tutorial across the breadth of artificial intelligence">
      <header className="hero hero--primary">
        <div className="container">
          <div className={styles.heroGrid}>
            <div>
              <p className={styles.eyebrow}>A living tutorial</p>
              <Heading as="h1" className={styles.title}>Artificial intelligence, mapped as a system.</Heading>
              <p className={styles.subtitle}>
                A public, evidence-first guide to learning paradigms, models, RAG, agents, skills, infrastructure, safety, autonomous networks, and the ideas connecting them.
              </p>
              <div className={styles.actions}>
                <Link className="button button--secondary button--lg" to="/docs/intro">Start the tutorial</Link>
                <Link className="button button--outline button--lg" to="/docs/updates">See daily updates</Link>
              </div>
            </div>
            <div className={styles.signal} aria-label="AI atlas signal diagram">
                <div className={`${styles.orbit} ${styles.orbitOne}`} />
                <div className={`${styles.orbit} ${styles.orbitTwo}`} />
              <div className={styles.core}>AI<br /><span>atlas</span></div>
              <div className={`${styles.node} ${styles.nodeTop}`}>learn</div>
              <div className={`${styles.node} ${styles.nodeRight}`}>retrieve</div>
              <div className={`${styles.node} ${styles.nodeBottom}`}>act</div>
              <div className={`${styles.node} ${styles.nodeLeft}`}>govern</div>
            </div>
          </div>
        </div>
      </header>
      <main>
        <section className="container">
          <div className={styles.featureGrid}>
            {features.map((feature) => (
              <Link className={styles.feature} to={feature.link} key={feature.title}>
                <Heading as="h2">{feature.title}</Heading>
                <p>{feature.text}</p>
                <span className={styles.arrow}>Explore →</span>
              </Link>
            ))}
          </div>
          <div className={styles.question}>
            <p className={styles.eyebrow}>The editorial question</p>
            <Heading as="h2">What changes when intelligence becomes infrastructure?</Heading>
            <p>Every chapter explains the technology, tests its limits, and connects it to evidence from the public research and industry landscape.</p>
          </div>
        </section>
      </main>
    </Layout>
  );
}
