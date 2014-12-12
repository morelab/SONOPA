# rule_system_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def concurrent(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('sensor_data', 'activity_level', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('concurrentActivations') >0:
          engine.assert_('sensor_data', 'processed',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def not_concurrent(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('sensor_data', 'activity_level', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('concurrentActivations') == 0:
          engine.assert_('sensor_data', 'processed',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def high_activity_level(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('sensor_data', 'test', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('activations') >=10:
          engine.assert_('sensor_data', 'activity_level',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def medium_activity_level(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('sensor_data', 'test', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('activations') >=5 and  10>context.lookup_data('activations'):
          engine.assert_('sensor_data', 'activity_level',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def low_activity_level(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('sensor_data', 'test', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('activations') >0 and  5>context.lookup_data('activations'):
          engine.assert_('sensor_data', 'activity_level',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('rule_system')
  
  fc_rule.fc_rule('concurrent', This_rule_base, concurrent,
    (('sensor_data', 'activity_level',
      (contexts.variable('activations'),
       contexts.variable('concurrentActivations'),),
      False),),
    (contexts.variable('activations'),
     pattern.pattern_literal('Mas de una'),))
  
  fc_rule.fc_rule('not_concurrent', This_rule_base, not_concurrent,
    (('sensor_data', 'activity_level',
      (contexts.variable('activations'),
       contexts.variable('concurrentActivations'),),
      False),),
    (contexts.variable('activations'),
     pattern.pattern_literal('cero'),))
  
  fc_rule.fc_rule('high_activity_level', This_rule_base, high_activity_level,
    (('sensor_data', 'test',
      (contexts.variable('activations'),
       contexts.variable('concurrentActivations'),),
      False),),
    (pattern.pattern_literal('High'),
     contexts.variable('concurrentActivations'),))
  
  fc_rule.fc_rule('medium_activity_level', This_rule_base, medium_activity_level,
    (('sensor_data', 'test',
      (contexts.variable('activations'),
       contexts.variable('concurrentActivations'),),
      False),),
    (pattern.pattern_literal('Medium'),
     contexts.variable('concurrentActivations'),))
  
  fc_rule.fc_rule('low_activity_level', This_rule_base, low_activity_level,
    (('sensor_data', 'test',
      (contexts.variable('activations'),
       contexts.variable('concurrentActivations'),),
      False),),
    (pattern.pattern_literal('Low'),
     contexts.variable('concurrentActivations'),))


Krb_filename = '../rule_system.krb'
Krb_lineno_map = (
    ((13, 17), (3, 3)),
    ((18, 18), (4, 4)),
    ((19, 21), (6, 6)),
    ((30, 34), (10, 10)),
    ((35, 35), (11, 11)),
    ((36, 38), (13, 13)),
    ((47, 51), (17, 17)),
    ((52, 52), (18, 18)),
    ((53, 55), (20, 20)),
    ((64, 68), (24, 24)),
    ((69, 69), (25, 25)),
    ((70, 72), (28, 28)),
    ((81, 85), (31, 31)),
    ((86, 86), (32, 32)),
    ((87, 89), (34, 34)),
)