import React from 'react';
import './CriteriaTree.css'; // Import a CSS file for styling

const Tree = ({ data }) => {
  const getDecisionClass = (decision) => {
    const decisionStr = typeof decision === 'string' ? decision.toLowerCase() : '';

    switch (decisionStr.toLowerCase()) {
      case 'true': return 'decision-true';
      case 'false': return 'decision-false';
      case 'uncertain': return 'decision-uncertain';
      default: return '';
    }
  };

  const renderCriteria = (criteria) => {
    if (!criteria) return null;

    return (
      <div className="criteria">
        {criteria.description && <div className={getDecisionClass(criteria.decision)}><strong>Criteria description:</strong> {criteria.description}</div>}

        {criteria.conjunction_sub_criteria && criteria.conjunction_sub_criteria.length > 0 && (
            <div>
                <strong>All of these must be true:</strong>
                {criteria.conjunction_sub_criteria.map((subCriteria, index) => (
                <div key={index} className="sub-criteria">
                    <Tree data={subCriteria} />
                </div>
                ))}
            </div>
            )}

        {criteria.disjunction_sub_criteria && criteria.disjunction_sub_criteria.length > 0 && criteria.disjunction_condition && 
          <div className="disjunction-condition">
            <strong> {criteria.disjunction_condition.operator} {criteria.disjunction_condition.value} of these must be true</strong>
          </div>
        }

        {criteria.disjunction_sub_criteria && criteria.disjunction_sub_criteria.map((subCriteria, index) => (
          <div key={index} className="sub-criteria">
            <Tree data={subCriteria} />
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className={`tree ${getDecisionClass(data.decision)}`}>
      <div><strong>Decision:</strong> {data.decision}</div>
      <div><strong>Reason:</strong> {data.reason}</div>
      {renderCriteria(data.criteria)}
    </div>
  );
};

export default Tree;
