from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/RequestGroup
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class RequestGroup(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A group of related requests.
    A group of related requests that can be used to capture intended activities
    that have inter-dependencies such as "give this medication after that one".
    """

    __resource_type__ = "RequestGroup"

    action: typing.List[fhirtypes.RequestGroupActionType] | None = Field(  # type: ignore
        default=None,
        alias="action",
        title="Proposed actions, if any",
        description="The actions, if any, produced by the evaluation of the artifact.",
        json_schema_extra={
            "element_property": True,
        },
    )

    author: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="author",
        title="Device or practitioner that authored the request group",
        description="Provides a reference to the author of the request group.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device", "Practitioner"],
        },
    )

    authoredOn: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="authoredOn",
        title="When the request group was authored",
        description="Indicates when the request group was created.",
        json_schema_extra={
            "element_property": True,
        },
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="basedOn",
        title="Fulfills plan, proposal, or order",
        description=(
            "A plan, proposal or order that is fulfilled in whole or in part by "
            "this request."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    context: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="context",
        title="Encounter or Episode for the request group",
        description="Describes the context of the request group, if any.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter", "EpisodeOfCare"],
        },
    )

    definition: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="definition",
        title="Instantiates protocol or definition",
        description=(
            "A protocol, guideline, orderset or other definition that is adhered to"
            " in whole or in part by this request."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    groupIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        default=None,
        alias="groupIdentifier",
        title="Composite request this is part of",
        description=(
            "A shared identifier common to all requests that were authorized more "
            "or less simultaneously by a single author, representing the identifier"
            " of the requisition, prescription or similar form."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Allows a service to provide a unique, business identifier for the "
            "request."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    intent: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="intent",
        title="proposal | plan | order",
        description=(
            "Indicates the level of authority/intentionality associated with the "
            "request and where the request fits into the workflow chain."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["proposal", "plan", "order"],
        },
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_intent", title="Extension field for ``intent``."
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        default=None,
        alias="note",
        title="Additional notes about the response",
        description=(
            "Provides a mechanism to communicate additional information about the "
            "response."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    priority: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the request should be addressed with respect to "
            "other requests."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["routine", "urgent", "asap", "stat"],
        },
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="reasonCodeableConcept",
        title="Reason for the request group",
        description=(
            "Indicates the reason the request group was created. This is typically "
            "provided as a parameter to the evaluation and echoed by the service, "
            "although for some use cases, such as subscription- or event-based "
            "scenarios, it may provide an indication of the cause for the response."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e reason[x]
            "one_of_many": "reason",
            "one_of_many_required": False,
        },
    )

    reasonReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="reasonReference",
        title="Reason for the request group",
        description=(
            "Indicates the reason the request group was created. This is typically "
            "provided as a parameter to the evaluation and echoed by the service, "
            "although for some use cases, such as subscription- or event-based "
            "scenarios, it may provide an indication of the cause for the response."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e reason[x]
            "one_of_many": "reason",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    replaces: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="replaces",
        title="Request(s) replaced by this request",
        description=(
            "Completed or terminated request(s) whose function is taken by this new"
            " request."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title=(
            "draft | active | suspended | cancelled | completed | entered-in-error "
            "| unknown"
        ),
        description=(
            "The current state of the request. For request groups, the status "
            "reflects the status of all the requests in the group."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "draft",
                "active",
                "suspended",
                "cancelled",
                "completed",
                "entered-in-error",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="subject",
        title="Who the request group is about",
        description="The subject for which the request group was created.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``RequestGroup`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "definition",
            "basedOn",
            "replaces",
            "groupIdentifier",
            "status",
            "intent",
            "priority",
            "subject",
            "context",
            "authoredOn",
            "author",
            "reasonCodeableConcept",
            "reasonReference",
            "note",
            "action",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``RequestGroup`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "identifier",
            "groupIdentifier",
            "status",
            "intent",
            "priority",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("intent", "intent__ext"), ("status", "status__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"reason": ["reasonCodeableConcept", "reasonReference"]}
        return one_of_many_fields


class RequestGroupAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Proposed actions, if any.
    The actions, if any, produced by the evaluation of the artifact.
    """

    __resource_type__ = "RequestGroupAction"

    action: typing.List[fhirtypes.RequestGroupActionType] | None = Field(  # type: ignore
        default=None,
        alias="action",
        title="Sub action",
        description="Sub actions.",
        json_schema_extra={
            "element_property": True,
        },
    )

    cardinalityBehavior: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="cardinalityBehavior",
        title="single | multiple",
        description="Defines whether the action can be selected multiple times.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["single", "multiple"],
        },
    )
    cardinalityBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_cardinalityBehavior",
        title="Extension field for ``cardinalityBehavior``.",
    )

    code: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="code",
        title="Code representing the meaning of the action or sub-actions",
        description=(
            "A code that provides meaning for the action or action group. For "
            "example, a section may have a LOINC code for a the section of a "
            "documentation template."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    condition: typing.List[fhirtypes.RequestGroupActionConditionType] | None = Field(  # type: ignore
        default=None,
        alias="condition",
        title="Whether or not the action is applicable",
        description=(
            "An expression that describes applicability criteria, or start/stop "
            "conditions for the action."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="Short description of the action",
        description=(
            "A short description of the action used to provide a summary to display"
            " to the user."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    documentation: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        default=None,
        alias="documentation",
        title="Supporting documentation for the intended performer of the action",
        description=(
            "Didactic or other informational resources associated with the action "
            "that can be provided to the CDS recipient. Information resources can "
            "include inline text commentary and links to web resources."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    groupingBehavior: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="groupingBehavior",
        title="visual-group | logical-group | sentence-group",
        description="Defines the grouping behavior for the action and its children.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["visual-group", "logical-group", "sentence-group"],
        },
    )
    groupingBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_groupingBehavior",
        title="Extension field for ``groupingBehavior``.",
    )

    label: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="label",
        title="User-visible label for the action (e.g. 1. or A.)",
        description="A user-visible label for the action.",
        json_schema_extra={
            "element_property": True,
        },
    )
    label__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_label", title="Extension field for ``label``."
    )

    participant: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="participant",
        title="Who should perform the action",
        description="The participant that should perform or be responsible for this action.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Person",
                "Practitioner",
                "RelatedPerson",
            ],
        },
    )

    precheckBehavior: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="precheckBehavior",
        title="yes | no",
        description="Defines whether the action should usually be preselected.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["yes", "no"],
        },
    )
    precheckBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_precheckBehavior",
        title="Extension field for ``precheckBehavior``.",
    )

    relatedAction: typing.List[fhirtypes.RequestGroupActionRelatedActionType] | None = Field(  # type: ignore
        default=None,
        alias="relatedAction",
        title="Relationship to another action",
        description=(
            'A relationship to another action such as "before" or "30-60 minutes '
            'after start of".'
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    requiredBehavior: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="requiredBehavior",
        title="must | could | must-unless-documented",
        description="Defines the requiredness behavior for the action.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["must", "could", "must-unless-documented"],
        },
    )
    requiredBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_requiredBehavior",
        title="Extension field for ``requiredBehavior``.",
    )

    resource: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="resource",
        title="The target of the action",
        description=(
            "The resource that is the target of the action (e.g. "
            "CommunicationRequest)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    selectionBehavior: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="selectionBehavior",
        title="any | all | all-or-none | exactly-one | at-most-one | one-or-more",
        description="Defines the selection behavior for the action and its children.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "any",
                "all",
                "all-or-none",
                "exactly-one",
                "at-most-one",
                "one-or-more",
            ],
        },
    )
    selectionBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_selectionBehavior",
        title="Extension field for ``selectionBehavior``.",
    )

    textEquivalent: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="textEquivalent",
        title=(
            "Static text equivalent of the action, used if the dynamic aspects "
            "cannot be interpreted by the receiving system"
        ),
        description=(
            "A text equivalent of the action to be performed. This provides a "
            "human-interpretable description of the action when the definition is "
            "consumed by a system that may not be capable of interpreting it "
            "dynamically."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    textEquivalent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_textEquivalent",
        title="Extension field for ``textEquivalent``.",
    )

    timingDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="timingDateTime",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_timingDateTime",
        title="Extension field for ``timingDateTime``.",
    )

    timingDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        default=None,
        alias="timingDuration",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="timingPeriod",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingRange: fhirtypes.RangeType | None = Field(  # type: ignore
        default=None,
        alias="timingRange",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        default=None,
        alias="timingTiming",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="title",
        title="User-visible title",
        description="The title of the action displayed to a user.",
        json_schema_extra={
            "element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_title", title="Extension field for ``title``."
    )

    type: fhirtypes.CodingType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="create | update | remove | fire-event",
        description="The type of action to perform (create, update, remove).",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``RequestGroupAction`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "label",
            "title",
            "description",
            "textEquivalent",
            "code",
            "documentation",
            "condition",
            "relatedAction",
            "timingDateTime",
            "timingPeriod",
            "timingDuration",
            "timingRange",
            "timingTiming",
            "participant",
            "type",
            "groupingBehavior",
            "selectionBehavior",
            "requiredBehavior",
            "precheckBehavior",
            "cardinalityBehavior",
            "resource",
            "action",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``RequestGroupAction`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "description", "textEquivalent"]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "timing": [
                "timingDateTime",
                "timingDuration",
                "timingPeriod",
                "timingRange",
                "timingTiming",
            ]
        }
        return one_of_many_fields


class RequestGroupActionCondition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether or not the action is applicable.
    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """

    __resource_type__ = "RequestGroupActionCondition"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="Natural language description of the condition",
        description=(
            "A brief, natural language description of the condition that "
            "effectively communicates the intended semantics."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="expression",
        title="Boolean-valued expression",
        description=(
            "An expression that returns true or false, indicating whether or not "
            "the condition is satisfied."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_expression", title="Extension field for ``expression``."
    )

    kind: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="kind",
        title="applicability | start | stop",
        description="The kind of condition.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["applicability", "start", "stop"],
        },
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_kind", title="Extension field for ``kind``."
    )

    language: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="language",
        title="Language of the expression",
        description="The media type of the language for the expression.",
        json_schema_extra={
            "element_property": True,
        },
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_language", title="Extension field for ``language``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``RequestGroupActionCondition`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "kind",
            "description",
            "language",
            "expression",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``RequestGroupActionCondition`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("kind", "kind__ext")]
        return required_fields


class RequestGroupActionRelatedAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationship to another action.
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """

    __resource_type__ = "RequestGroupActionRelatedAction"

    actionId: fhirtypes.IdType | None = Field(  # type: ignore
        default=None,
        alias="actionId",
        title="What action this is related to",
        description="The element id of the action this is related to.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    actionId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_actionId", title="Extension field for ``actionId``."
    )

    offsetDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        default=None,
        alias="offsetDuration",
        title="Time offset for the relationship",
        description=(
            "A duration or range of durations to apply to the relationship. For "
            "example, 30-60 minutes before."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e offset[x]
            "one_of_many": "offset",
            "one_of_many_required": False,
        },
    )

    offsetRange: fhirtypes.RangeType | None = Field(  # type: ignore
        default=None,
        alias="offsetRange",
        title="Time offset for the relationship",
        description=(
            "A duration or range of durations to apply to the relationship. For "
            "example, 30-60 minutes before."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e offset[x]
            "one_of_many": "offset",
            "one_of_many_required": False,
        },
    )

    relationship: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="relationship",
        title=(
            "before-start | before | before-end | concurrent-with-start | "
            "concurrent | concurrent-with-end | after-start | after | after-end"
        ),
        description="The relationship of this action to the related action.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "before-start",
                "before",
                "before-end",
                "concurrent-with-start",
                "concurrent",
                "concurrent-with-end",
                "after-start",
                "after",
                "after-end",
            ],
        },
    )
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_relationship",
        title="Extension field for ``relationship``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``RequestGroupActionRelatedAction`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "actionId",
            "relationship",
            "offsetDuration",
            "offsetRange",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``RequestGroupActionRelatedAction`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("actionId", "actionId__ext"),
            ("relationship", "relationship__ext"),
        ]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"offset": ["offsetDuration", "offsetRange"]}
        return one_of_many_fields
